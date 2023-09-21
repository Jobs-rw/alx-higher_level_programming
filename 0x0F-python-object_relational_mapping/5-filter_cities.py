#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all cities """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities c
                LEFT JOIN states s ON c.state_id = s.id
                WHERE s.name LIKE BINARY %s
                ORDER BY c.id ASC""", (argv[4],))
    row = cur.fetchone()
    lista = []
    while row is not None:
        lista.append(row[0])
        row = cur.fetchone()
    print(", ".join(lista))
    cur.close()
    db.close()
