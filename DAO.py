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
        genre = session.query(Genre).filter(Genre.id == id).first()
        return genre
    
class DAOCompanies():
    
    def select(session, id):
        company = session.query(Company).filter(Company.id == id).first()
        return company
    
class DAOGames():
    
    def select(session, id):
        game = session.query(Game).filter(Game.id == id).first()
        return game
    