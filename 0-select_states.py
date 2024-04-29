#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa."""

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
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of lists.
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
