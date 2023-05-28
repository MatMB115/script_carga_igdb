# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError

from DAO import *
from mapeamento import *

from igdb.wrapper import IGDBWrapper
import json
import requests
from datetime import datetime
from iso3166 import countries_by_numeric

class AcessDB:
    def insert(plat):
        try:
            session = DAO.getSession()
            DAO.insert(session, plat)
            session.commit()
            session.close()
            return 1
        except:
            return 0

    def selectPlat(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            plat = DAOPlataform.select(session, id)
            session.commit()
            session.close()
            return plat
        except:
            return 0
    
    def selectGenre(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            genre = DAOGenres.select(session, id)
            session.commit()
            session.close()
            return genre
        except:
            return 0
        
    def selectCompany(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            company = DAOCompanies.select(session, id)
            session.commit()
            session.close()
            return company
        except:
            return 0

        
class AcessToken:
    def __init__(self):
        self.clientId = 'cividn0xlqz29fotpopze64bjpqk0y'
        self.clientSecret = '7qeh1o0kzz9rjaf4ua3rubh7fws337'
        self.acessToken = None
    
    def generateToken(self):
        # Set up the OAuth token endpoint URL
        oauth_url = 'https://id.twitch.tv/oauth2/token'
        params = {
            'grant_type': 'client_credentials',
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
        }
        # Send the OAuth token endpoint request and parse the response
        try:
            response = requests.post(oauth_url, params=params)
            response_data = response.json()

            # Extract the access token from the response data
            access_token = response_data['access_token']
            self.acessToken = access_token
            return 1
        except Exception as e:
            return repr(e)

    def getClientId(self):
        return self.clientId
    
    def getToken(self):
        return self.acessToken
    
class API:
    def __init__(self, token):
        self.token = token
        self.manipulateDB = AcessDB

    def formatCountryIso(self, company):
        country = countries_by_numeric.get(str(company['country']))
        if country != None:
            company['country'] = country[0]
        else:
            company['country'] = 'N/A'

    def formatDate(self, plat):
        plat['created_at'] = datetime.fromtimestamp(plat['created_at']).strftime('%Y-%m-%d')
        plat['updated_at'] = datetime.fromtimestamp(plat['updated_at']).strftime('%Y-%m-%d')

    def getPlataforms(self):
        try:
            #Wrapper da biblioteca Apicalyse que suporta a API do IGDB
            wrapper = IGDBWrapper(self.token.getClientId(), self.token.getToken())
            byte_array = wrapper.api_request(
                'platforms',
                'fields id, name, abbreviation, alternative_name, generation, created_at, updated_at; limit 200;'#200
            )
            platforms_json = json.loads(byte_array)
            
            #Se por algum motivo retornar um json vazio, lança a exception
            if len(platforms_json) == 0:
                raise Exception('Returned json is empty')
                
            print('Fazendo a carga das plataformas no banco...')

            for plat in platforms_json:
                #Tratar a data (Timestamp) fornecida pela API
                self.formatDate(plat)
                if not plat.get('generation'):
                    plat['generation'] = 1
                if not plat.get('alternative_name'):
                    plat['alternative_name'] = 'N/A'
                if not plat.get('abbreviation'):
                    plat['abbreviation'] = 'N/A'
                #Criar objeto do tipo plataforma
                platObject = Plataform(id=int(plat['id']),
                                        name=str(plat['name']),
                                        created_at=str(plat['created_at']),
                                        updated_at=str(plat['updated_at']),
                                        abbreviation=str(plat['abbreviation']),
                                        alternative_name=str(plat['alternative_name']),
                                        generation=int(plat['generation']))

                #Verifica se o objeto já existe no banco
                check = self.manipulateDB.selectPlat(platObject.id)
                id = str(platObject.id)
                if not check:
                    self.manipulateDB.insert(platObject)
                    print('Plataforma inserida no banco. ID: ' + id)
                else:
                    print('Plataforma já existe no banco. ID: ' + id)
                    
            return 1
              
        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)
        
    def getGenres(self):
        try:
            #Wrapper da biblioteca Apicalyse que suporta a API do IGDB
            wrapper = IGDBWrapper(self.token.getClientId(), self.token.getToken())
            byte_array = wrapper.api_request(
                'genres',
                'fields id, name, created_at, updated_at, url; limit 25;'#22
            )
            genres_json = json.loads(byte_array)
            
            #Se por algum motivo retornar um json vazio, lança a exception
            if len(genres_json) == 0:
                raise Exception('Returned json is empty')

            print('Fazendo a carga dos gêneros no banco...')

            for genre in genres_json:
                #Tratar a data (Timestamp) fornecida pela API
                self.formatDate(genre)
                #Criar objeto do tipo plataforma
                genreObject = Genre(id=int(genre['id']),
                                        name=str(genre['name']),
                                        created_at=str(genre['created_at']),
                                        updated_at=str(genre['updated_at']),
                                        url = str(genre['url']))

                #Verifica se o objeto já existe no banco
                check = self.manipulateDB.selectGenre(genreObject.id)
                id = str(genreObject.id)
                if not check:
                    self.manipulateDB.insert(genreObject)
                    print('Genero inserido no banco. ID: ' + id)
                else:
                    print('Genero já existe no banco. ID: ' + id)
                    
            return 1
              
        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)
    
    def getCompanies(self):
        try:
            #Wrapper da biblioteca Apicalyse que suporta a API do IGDB
            wrapper = IGDBWrapper(self.token.getClientId(), self.token.getToken())
            offset = 0
            while offset < 45700:
                request = 'fields id, name, created_at, updated_at, country; limit 500; offset ' + str(offset) + ';'
                byte_array = wrapper.api_request(
                    'companies',
                    request
                )
                companies_json = json.loads(byte_array)
                
                #Se por algum motivo retornar um json vazio, lança a exception
                if len(companies_json) == 0:
                    raise Exception('Returned json is empty')
                
                print('Fazendo a carga das companhias no banco...')

                for company in companies_json:
                    #Tratar a data (Timestamp) fornecida pela API
                    self.formatDate(company)
                    
                    if company.get('country'):
                        #Tratar a ISO3166-1 Alpha-2 fornecida pela API
                        self.formatCountryIso(company)
                    else:
                        company['country'] = 'N/A'
                    
                    #Criar objeto do tipo companhia 
                    companyObject = Company(id=int(company['id']),
                                            name=str(company['name']),
                                            created_at=str(company['created_at']),
                                            updated_at=str(company['updated_at']),
                                            country=str(company['country']))
                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectCompany(companyObject.id)
                    id = str(companyObject.id)
                    if not check:
                        self.manipulateDB.insert(companyObject)
                        print('Companhia inserida no banco. ID: ' + id)
                    else:
                        print('Companhia já existe no banco. ID: ' + id)
                #Incrementa o offset para pegar os próximos 500 registros até o limite de 45500
                if offset == 45500:
                    offset += 123 #soma para o último offset
                else:
                    offset += 500
                    
            return 1
              
        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)
        
