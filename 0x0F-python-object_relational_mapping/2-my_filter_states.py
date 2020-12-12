#!/usr/bin/python3
"""
Filter the states with user input
"""


import MySQLdb as mdb
import sys

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
con = mdb.connect('localhost', user, password, database)

if __name__ == "__main__":
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format
            (sys.argv[4]))

        rows = cur.fetchall()

        for row in rows:
            print(row)
