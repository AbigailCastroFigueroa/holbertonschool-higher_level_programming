#!/usr/bin/python3
"""Scrip to perform an update to a database."""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    data_to_delete = session.query(State).filter(
        or_(State.name.like('a%'), State.name.like('%a%')))
    for item in data_to_delete:
        session.delete(item)
    session.commit()
