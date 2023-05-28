# coding: utf-8
from sqlalchemy import Column, Date, Integer, SmallInteger, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'companies'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    country = Column(String(40))
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)


class Genre(Base):
    __tablename__ = 'genres'
    __table_args__ = {'schema': 'public'}

    id = Column(SmallInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    url = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)


class Plataform(Base):
    __tablename__ = 'plataform'
    __table_args__ = {'schema': 'public'}

    id = Column(SmallInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    abbreviation = Column(String(50))
    alternative_name = Column(String(100))
    generation = Column(SmallInteger)
