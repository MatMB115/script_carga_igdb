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

    def selectGames(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            game = DAOGames.select(session, id)
            session.commit()
            session.close()
            return game
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
            while offset < 45600:
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
                offset += 500
                    
            return 1
              
        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)
        
    def getGames(self):
        try:
            #Wrapper da biblioteca Apicalyse que suporta a API do IGDB
            wrapper = IGDBWrapper(self.token.getClientId(), self.token.getToken())
            #Recuperar os modos de jogo
            byte_array = wrapper.api_request(
                'game_modes',
                'fields id, name; limit 10;'
            )
            modes_json = json.loads(byte_array)

            #Se por algum motivo retornar um json vazio, lança a exception
            if len(modes_json) == 0:
                raise Exception('Returned game modes json is empty')
            
            #Recuperar os motores de jogo
            offset = 0
            engines_json = []
            while offset < 1001:
                request = 'fields id, name; limit 500; offset ' + str(offset) + ';'
                byte_array = wrapper.api_request(
                'game_engines',
                request
                )
                engines_json.extend(json.loads(byte_array))
                offset += 500
            
            #Se por algum motivo retornar um json vazio, lança a exception
            if len(engines_json) == 0:
                raise Exception('Returned game engines json is empty')
            
            #Recuperar os jogos
            print('Fazendo a carga dos games no banco...')

            #Contadores para ter controle da quantidade de jogos inseridos no banco e dos jogos que não foram inseridos
            noInsertedByCompany = 0
            noRelationWithCompany = 0
            noRelationWithGenre = 0
            noRelationWithPlat = 0
            offset = 0

            while offset < 120000:
                request = 'fields id, name, summary, genres, platforms, created_at, updated_at, game_engines, url, game_modes, first_release_date, involved_companies, follows; limit 500; offset ' + str(offset) + ';'
                byte_array = wrapper.api_request(
                    'games',
                    request
                )
                games_json = json.loads(byte_array)
                
                for game in games_json:
                    #Verificar se o jogo tem um companhia envolvida
                    if game.get('involved_companies'):
                        #Recuperar a companhia envolvida
                        company = game['involved_companies'][0]

                        #Verificar se a companhia existe no banco
                        companyObject = self.manipulateDB.selectCompany(company)
                        if not companyObject:
                            print('Companhia não existe no banco. ID: ' + str(company))
                            noInsertedByCompany += 1
                        else:
                            #Tem companhia envolvida, jogo pode ser inserido no banco
                            #Tratar a data (Timestamp) fornecida pela API
                            self.formatDate(game)

                            #Tratar a data (Timestamp) fornecida pela API
                            if game.get('first_release_date'):
                                game['first_release_date'] = datetime.fromtimestamp(game['first_release_date']).strftime('%Y-%m-%d')
                            else:
                                game['first_release_date'] = 'N/A'
                                
                            #Tratar o summary
                            if not game.get('summary'):
                                game['summary'] = 'N/A'

                            #Tratar se há motores de jogo e modos de jogo
                            if not game.get('game_engines'):
                                game['game_engines'] = 'N/A'
                            else:
                                #Recuperar o nome do motor de jogo
                                for engine in engines_json:
                                    if engine['id'] == game['game_engines'][0]:
                                        game['game_engines'] = engine['name']
                                        break

                            if not game.get('game_modes'):
                                game['game_modes'] = 'N/A'
                            else:
                                #Recuperar o nome do modo de jogo
                                for mode in modes_json:
                                    if mode['id'] == game['game_modes'][0]:
                                        game['game_modes'] = mode['name']
                                        break
                            #Tratar o follows
                            if not game.get('follows'):
                                game['follows'] = 0

                            #Criar objeto do tipo jogo
                            gameObject = Game(id=int(game['id']),
                                                name=str(game['name']),
                                                created_at=str(game['created_at']),
                                                updated_at=str(game['updated_at']),
                                                url=str(game['url']),
                                                game_engines=str(game['game_engines']),
                                                game_modes=str(game['game_modes']),
                                                summary=str(game['summary']),
                                                follows=int(game['follows']),
                                                release_date=str(game['first_release_date']))
                            #Verifica se o objeto já existe no banco
                            check = self.manipulateDB.selectGames(gameObject.id)
                            id = gameObject.id

                            if not check:
                                #Adicionar o relacionamento das companhias envolvidas
                                for company in game['involved_companies']:
                                    companyObject = self.manipulateDB.selectCompany(int(company))
                                    if not companyObject:
                                        noRelationWithCompany += 1
                                    else:
                                        gameObject.companies.append(companyObject)

                                #Adicionar o relacionamento dos gêneros
                                if game.get('genres'):
                                    for genre in game['genres']:
                                        genreObject = self.manipulateDB.selectGenre(genre)
                                        if not genreObject:
                                            noRelationWithGenre += 1
                                        else:
                                            gameObject.genres.append(genreObject)
                                else:
                                    print('Jogo não possui gênero. ID: ' + str(game['id']))

                                #Adicionar o relacionamento das plataformas
                                if game.get('platforms'):
                                    for plat in game['platforms']:
                                        platObject = self.manipulateDB.selectPlat(plat)
                                        if not platObject:
                                            noRelationWithPlat += 1
                                        else:
                                            gameObject.plataform.append(platObject)
                                else:
                                    print('Jogo não possui plataforma. ID: ' + str(game['id']))

                                self.manipulateDB.insert(gameObject)
                                print('Jogo inserido no banco. ID: ' + str(id))

                            else:
                                print('Jogo já existe no banco. ID: ' + str(id))
                    else :
                        print('Jogo não possui companhia envolvida. ID: ' + str(game['id']))
                        noInsertedByCompany += 1
                offset += 500
            return 1

        except Exception as e:
            return 'Lembre-se de gerar o token primeiro.\nERRO: ' + repr(e)