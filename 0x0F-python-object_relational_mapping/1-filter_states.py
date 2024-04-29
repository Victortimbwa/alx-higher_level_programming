#!/usr/bin/python3
"""A script that lists all states with names starting with
'N' from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    query = ("SELECT * FROM states WHERE name LIKE binary 'N%'\
    ORDER BY states.id ASC")

    cur.execute(query)

    # Fetch all results
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
