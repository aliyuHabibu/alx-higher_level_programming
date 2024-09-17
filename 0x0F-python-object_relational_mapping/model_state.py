#!/usr/bin/python3
""" Module that defines a class which is
    mapped to a database table
"""
# Inporting Utilities
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

# Declaring the mapper
Base = declarative_base()

# Defining the class
class State(Base):
    """ Class definition with class attributes """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
