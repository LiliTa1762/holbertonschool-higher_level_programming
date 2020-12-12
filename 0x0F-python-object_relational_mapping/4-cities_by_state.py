#!/usr/bin/python3
"""
Getting all states of a DB
"""


import MySQLdb as mdb
import sys

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
con = mdb.connect('localhost', user, password, database)

with con:
    cur = con.cursor()
    cur.execute(
		"SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    rows = cur.fetchall()

    for row in rows:
	    print(row)
