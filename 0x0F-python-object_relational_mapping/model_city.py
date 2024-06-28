#!/usr/bin/python3
"""
This module defines the City class which maps to the cities table in hbtn_0e_14_usa database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """ City class to map to the cities table in the database """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

