#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    state_name = sys.argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities "
                   "LEFT JOIN states "
                   "ON states.id = cities.state_id "
                   "WHERE states.name LIKE BINARY (%s) "
                   "ORDER BY cities.id ASC",
                   (state_name,))

    rows = cursor.fetchall()
    cursor.close()
    db.close()

    str_cities = ", ".join(row[0] for row in rows)

    print(str_cities)
