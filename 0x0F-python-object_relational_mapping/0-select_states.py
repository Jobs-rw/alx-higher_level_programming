#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple separate working environments
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    row = cur.fetchone()  # Initialize row with the first row
    while row is not None:
        print(row)
        row = cur.fetchone()  # Fetch the next row

    # Clean up process
    cur.close()
    db.close()
