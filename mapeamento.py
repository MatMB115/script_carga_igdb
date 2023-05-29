# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, SmallInteger, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Character(Base):
    __tablename__ = 'character'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    url = Column(Text, nullable=False)

    games = relationship('Game', secondary='public.game_character')


class Company(Base):
    __tablename__ = 'companies'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    country = Column(Text)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    

class Game(Base):
    __tablename__ = 'games'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    url = Column(Text, nullable=False)
    game_modes = Column(Text)
    summary = Column(Text)
    game_engines = Column(Text)
    follows = Column(Integer)
    release_date = Column(Date)

    companies = relationship('Company', secondary='public.game_company')
    plataform = relationship('Plataform', secondary='public.game_plataform')
    genres = relationship('Genre', secondary='public.game_genre')


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


t_game_character = Table(
    'game_character', metadata,
    Column('id_game', ForeignKey('public.games.id'), nullable=False),
    Column('id_character', ForeignKey('public.character.id'), nullable=False),
    schema='public'
)


t_game_company = Table(
    'game_company', metadata,
    Column('id_game', ForeignKey('public.games.id'), nullable=False),
    Column('id_company', ForeignKey('public.companies.id'), nullable=False),
    schema='public'
)


t_game_genre = Table(
    'game_genre', metadata,
    Column('id_game', ForeignKey('public.games.id'), nullable=False),
    Column('id_genre', ForeignKey('public.genres.id'), nullable=False),
    schema='public'
)


t_game_plataform = Table(
    'game_plataform', metadata,
    Column('id_game', ForeignKey('public.games.id'), nullable=False),
    Column('id_plataform', ForeignKey('public.plataform.id'), nullable=False),
    schema='public'
)
