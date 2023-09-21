#!/usr/bin/python3
"""
the Script that takes in the name of a state and lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

# codes will  not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    row = cur.fetchone()
    j = []
    while row is not None:
        j.append(row[1])
        row = cur.fetchone()

    print(", ".join(j))

    # Clean up process
    cur.close()
    db.close()
