# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, SmallInteger, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


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


class PlataformVersion(Base):
    __tablename__ = 'plataform_version'
    __table_args__ = {'schema': 'public'}

    id = Column(SmallInteger, primary_key=True)
    name = Column(Text, nullable=False)
    os = Column(Text)
    memory = Column(Text)
    cpu = Column(Text)
    graphics = Column(Text)
    sound = Column(Text)
    connectivity = Column(Text)
    resolution = Column(Text)
    plataform = Column(ForeignKey('public.plataform.id'))

    plataform1 = relationship('Plataform')
