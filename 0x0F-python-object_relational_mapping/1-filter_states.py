#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and print rows using a while loop
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()

    # Clean up process
    cur.close()
    db.close()
