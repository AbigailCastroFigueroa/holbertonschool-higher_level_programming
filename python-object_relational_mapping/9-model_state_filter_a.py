#!/usr/bin/python3
"""Show a list of the first object from a database."""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).filter(
        or_(State.name.like('a%'), State.name.like('%a%'))).order_by(State.id)
    for item in data:
        id, name = item.id, item.name
        print(f"{id}: {name}")
