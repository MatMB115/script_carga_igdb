from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *

class DAOPlataform():
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:fabosmati@localhost:5432/IGDB")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def insert(session, obj):
        session.add(obj)

    def select(session, id):
        plat = session.query(Plataform).filter(Plataform.id == id).first()
        return plat
