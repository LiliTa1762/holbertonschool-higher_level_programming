#!/usr/bin/python3
"""Contains 'a'
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

    rs = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()

    for row in rs:
        print("{}: {}".format(row.id, row.name))

    session.close()
