import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False, unique=True)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)    


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planets')

    def to_dict(self):
        return {}


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    year = Column(DateTime)
    planet_id = Column(Integer, ForeignKey('planet.id'))


class CharactersFilms(Base):
    __tablename__ = 'characters_films'
    id = Column(Integer, primary_key=True)
    minutes = Column(DateTime)
    character_id = Column(Integer, ForeignKey('characters.id'))
    film_id = Column(Integer, ForeignKey('films.id'))
    character = relationship('Characters', foreign_keys=['character_id'])  # falta el parametro del foreignkey
    film = relationship('Films', foreign_keys=['film_id'])  # falta el parametro del foreignkey


class CharacterFavorites(Base):
    __tablename__ = 'character_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)


class PlanetFavorites(Base):
    __tablename__ = 'Planet_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
