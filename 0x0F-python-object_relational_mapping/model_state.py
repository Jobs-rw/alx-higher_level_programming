#!/usr/bin/python3
"""
This file is containing of  the class definition of a State and an instance
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Attributes:
        id: Id state
        name: Name of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(130), nullable=False)
