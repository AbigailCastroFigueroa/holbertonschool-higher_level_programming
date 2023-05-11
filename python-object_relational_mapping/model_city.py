#!/usr/bin/python3
"""Creating a class using sqlalchemy."""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Creating class State."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


if __name__ == '__main__':
    engine = create_engine('mysql://Holberton@localhost/3306/')
    Base.metadata.create_all(engine)
