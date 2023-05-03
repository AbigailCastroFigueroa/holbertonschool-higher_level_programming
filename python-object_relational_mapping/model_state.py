#!/usr/bin/python3
"""Creating a class using sqlalchemy."""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Creating class State."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128))


if __name__ == '__main__':
    engine = create_engine('mysql://Holberton@localhost/3306/')
    Base.metadata.create_all(engine)
