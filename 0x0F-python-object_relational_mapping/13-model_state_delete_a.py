#!/usr/bin/python3
"""Deletes all State objects with a name containing a letter from a database
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    rs = session.query(State).filter(State.name.contains('a')).all()

    for result in rs:
        session.delete(result)

    session.commit()

    session.close()
