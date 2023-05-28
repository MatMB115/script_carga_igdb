# coding: utf-8
from datetime import datetime
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

class AcessDB:
    def insertPlat(plat):
        try:
            session = DAOPlataform.getSession()
            DAOPlataform.insert(session, plat)
            session.commit()
            session.close()
            return 1
        except:
            return 0

    def selectPlat(id):
        try:
            session = DAOPlataform.getSession()
            session.expire_on_commit = False
            plat = DAOPlataform.select(session, id)
            session.commit()
            session.close()
            return plat
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
            print('Fazendo a carga das plataformas no banco...')
            #Se por algum motivo retornar um json vazio, lança a exception
            if len(platforms_json) == 0:
                raise Exception('Returned json is empty')
                
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
                    self.manipulateDB.insertPlat(platObject)
                    print('Plataforma inserida no banco. ID: ' + id)
                else:
                    print('Plataforma já existe no banco. ID: ' + id)
                    
            return 1
              
        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)
        
    def getPlataformVersion(self):
        try:
            wrapper = IGDBWrapper(self.token.getClientId(), self.token.getToken())
            byte_array = wrapper.api_request(
                'platform_versions',
                'fields id, name, os, memory, cpu, graphics, sound, connectivity, resolutions; limit 200;'#200
            )
            platforms_json = json.loads(byte_array)
            print('Fazendo a carga das versões das plataformas no banco...')
            #Se por algum motivo retornar um json vazio, lança a exception
            if len(platforms_json) == 0:
                raise Exception('Returned json is empty')
                
            for plat in platforms_json:
                print(plat)
                    
            return 1
              
        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)