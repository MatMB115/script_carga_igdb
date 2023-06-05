from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *

class DAO():
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:fabosmati@localhost:5432/IGDB")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    
    def insert(session, obj):
        session.add(obj)

class DAOPlataform():
    
    def select(session, id):
        plat = session.query(Plataform).filter(Plataform.id == id).first()
        return plat

class DAOGenres():
    
    def select(session, id):
        genre = session.query(Genres).filter(Genres.id == id).first()
        return genre
    
class DAOCompanies():
    
    def select(session, id):
        company = session.query(Companies).filter(Companies.id == id).first()
        return company
    
class DAOGames():
    
    def select(session, id):
        game = session.query(Games).filter(Games.id == id).first()
        return game
    
class DAOCharacter():
    
    def select(session, id):
        chara = session.query(Character).filter(Character.id == id).first()
        return chara
    
class DAOGamesModes():
    
    def select(session, id):
        mode = session.query(GamesModes).filter(GamesModes.id == id).first()
        return mode
    