#!/usr/bin/python3
"""
Filter the states
"""


import MySQLdb as mdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    con = mdb.connect('localhost', port= 3306, user, password, database)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

        rows = cur.fetchall()

        for row in rows:
            print(row)
