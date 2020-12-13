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
    con = mdb.connect('localhost', user, password, database)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cur.fetchall()

        for row in rows:
            if row[1][0] is 'N':
                print(row)
