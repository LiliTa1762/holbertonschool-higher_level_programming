#!/usr/bin/python3
"""
Filter the states with user input
"""


import MySQLdb as mdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    con = mdb.connect('localhost', user, password, database)

    cur = con.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    con.close()
