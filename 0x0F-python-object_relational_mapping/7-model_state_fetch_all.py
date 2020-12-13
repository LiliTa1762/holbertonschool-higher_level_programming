#!/usr/bin/python3
"""Class definition of State
"""


from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys


engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.
    format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

con = engine.connect()

rs = con.execute("SELECT * from states ORDER BY id ASC")

row = rs.fetchone()
for row in rs:
    print('{:d}: {:s}'.format(row[0], row[1]))
