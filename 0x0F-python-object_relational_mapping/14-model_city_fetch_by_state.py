#!/usr/bin/python3
"""Prints all City objects from database
"""


from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    rs = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for row, rows in rs:
        print("{}: ({}) {}".format(rows.name, row.id, row.name))

    session.close()
