#!/usr/bin/python3
"""
Getting all states of a DB
"""


import MySQLdb as mdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    con = mdb.connect('localhost', user, password, database)

    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")

        rows = cur.fetchall()

        list_cities = []
        for row in rows:
            if row[1] == sys.argv[4]:
                list_cities.append(row[0])
        print(', '.join(list_cities))
