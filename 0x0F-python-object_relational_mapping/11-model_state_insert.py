#!/usr/bin/python3
"""Adds a State object to the database 
"""


from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    cl = State(name="Louisiana")

    session.add(cl)
    session.commit()

    rs = session.query(State).all()

    print(len(rs))

    session.close()
