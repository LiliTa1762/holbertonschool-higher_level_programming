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
        cur.execute("SELECT * FROM states ORDER BY states.id")

        rows = cur.fetchall()

        for row in rows:
            print(row)
