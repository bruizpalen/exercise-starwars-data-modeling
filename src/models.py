import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable= True)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    population = Column(Integer, nullable =False)
    terrain = Column(Integer, nullable=False)
    # post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    capacity = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

class FavoritePeople(Base):
    __tablename__ = 'favorite_people'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))

class FavoriteVehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column (Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id= Column(Integer, ForeignKey('planets.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
