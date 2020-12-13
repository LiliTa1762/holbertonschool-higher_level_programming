#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database
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

    rs = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).first()

    if rs:
        print(rs.id)
    else:
        print("Not found")

    session.close()
