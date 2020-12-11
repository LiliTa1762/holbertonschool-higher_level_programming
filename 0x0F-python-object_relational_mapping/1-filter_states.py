#!/usr/bin/python3
"""
Filter the states
"""


import MySQLdb as mdb
import sys

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
con = mdb.connect('localhost', user, password, database)

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name ='N"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  """
