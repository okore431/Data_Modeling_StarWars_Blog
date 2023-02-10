import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    password = Column (String(40), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    favorites = relationship("Favorites", back_populates="user")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), ForeignKey('user.username'))
    planets = Column(String(250), ForeignKey('planet.name'))
    characters = Column(String(250), ForeignKey('characters.name'))  

class Planets(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    planet_name = Column(String(250), nullable=False)
    population = Column(Integer)
    gravity = Column(String(40))
    climate = Column(String(50))
    terrain = Column(String(50))
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    favorites = relationship("Favorites", back_populates="planets")

class Characters (Base) :
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    height = Column (Integer)
    weight = Column (Integer)
    eye_color = Column (String(10))
    favorites = relationship("Favorites", back_populates="characters")

def to_dict(self):
    return {}
        
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
