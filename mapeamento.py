from sqlalchemy import Column, Date, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class Character(Base):
    __tablename__ = 'character'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='character_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    name = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    url = Column(Text, nullable=False)

    games = relationship('Games', secondary='public.game_character', back_populates='character')


class Companies(Base):
    __tablename__ = 'companies'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='companies_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    name = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    country = Column(Text)

    games = relationship('Games', secondary='public.game_company', back_populates='companies')


class Games(Base):
    __tablename__ = 'games'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='games_pkey'),
        {'schema': 'public'}
    )

    id = Column(Integer)
    name = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    url = Column(Text, nullable=False)
    summary = Column(Text)
    game_engines = Column(Text)
    follows = Column(Integer)
    release_date = Column(Date)

    character = relationship('Character', secondary='public.game_character', back_populates='games')
    companies = relationship('Companies', secondary='public.game_company', back_populates='games')
    games_modes = relationship('GamesModes', secondary='public.game_gamemode', back_populates='games')
    genres = relationship('Genres', secondary='public.game_genre', back_populates='games')
    plataform = relationship('Plataform', secondary='public.game_plataform', back_populates='games')


class GamesModes(Base):
    __tablename__ = 'games_modes'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='games_modes_pkey'),
        UniqueConstraint('name', name='games_modes_name_key'),
        {'schema': 'public'}
    )

    id = Column(SmallInteger)
    name = Column(String(40), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    url = Column(Text, nullable=False)

    games = relationship('Games', secondary='public.game_gamemode', back_populates='games_modes')


class Genres(Base):
    __tablename__ = 'genres'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='genres_pkey'),
        UniqueConstraint('name', name='genres_name_key'),
        {'schema': 'public'}
    )

    id = Column(SmallInteger)
    name = Column(String(100), nullable=False)
    url = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)

    games = relationship('Games', secondary='public.game_genre', back_populates='genres')


class Plataform(Base):
    __tablename__ = 'plataform'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='plataform_pkey'),
        {'schema': 'public'}
    )

    id = Column(SmallInteger)
    name = Column(String(100), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    abbreviation = Column(String(50))
    alternative_name = Column(String(100))
    generation = Column(SmallInteger)

    games = relationship('Games', secondary='public.game_plataform', back_populates='plataform')


t_game_character = Table(
    'game_character', metadata,
    Column('id_game', Integer, nullable=False),
    Column('id_character', Integer, nullable=False),
    ForeignKeyConstraint(['id_character'], ['public.character.id'], name='game_character_id_character_fkey'),
    ForeignKeyConstraint(['id_game'], ['public.games.id'], name='game_character_id_game_fkey'),
    schema='public'
)


t_game_company = Table(
    'game_company', metadata,
    Column('id_game', Integer, nullable=False),
    Column('id_company', Integer, nullable=False),
    ForeignKeyConstraint(['id_company'], ['public.companies.id'], name='game_company_id_company_fkey'),
    ForeignKeyConstraint(['id_game'], ['public.games.id'], name='game_company_id_game_fkey'),
    schema='public'
)


t_game_gamemode = Table(
    'game_gamemode', metadata,
    Column('id_game', Integer, nullable=False),
    Column('id_game_mode', SmallInteger, nullable=False),
    ForeignKeyConstraint(['id_game'], ['public.games.id'], name='game_gamemode_id_game_fkey'),
    ForeignKeyConstraint(['id_game_mode'], ['public.games_modes.id'], name='game_gamemode_id_game_mode_fkey'),
    schema='public'
)


t_game_genre = Table(
    'game_genre', metadata,
    Column('id_game', Integer, nullable=False),
    Column('id_genre', SmallInteger, nullable=False),
    ForeignKeyConstraint(['id_game'], ['public.games.id'], name='game_genre_id_game_fkey'),
    ForeignKeyConstraint(['id_genre'], ['public.genres.id'], name='game_genre_id_genre_fkey'),
    schema='public'
)


t_game_plataform = Table(
    'game_plataform', metadata,
    Column('id_game', Integer, nullable=False),
    Column('id_plataform', SmallInteger, nullable=False),
    ForeignKeyConstraint(['id_game'], ['public.games.id'], name='game_plataform_id_game_fkey'),
    ForeignKeyConstraint(['id_plataform'], ['public.plataform.id'], name='game_plataform_id_plataform_fkey'),
    schema='public'
)
