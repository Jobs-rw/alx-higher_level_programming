#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple separate working environments
    # through the same connection to the database.
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()

    # Clean up process
    cur.close()
    db.close()
