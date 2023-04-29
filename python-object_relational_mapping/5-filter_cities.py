#!/usr/bin/python3
"""Using join to select data from a database using python script."""
import sys
import MySQLdb

if __name__ == '__main__':
    my_host = "localhost"
    my_user = sys.argv[1]
    my_pwd = sys.argv[2]
    my_database = sys.argv[3]

    working_database = MySQLdb.connect(
        host=my_host, user=my_user, password=my_pwd, db=my_database, port=3306)

    cur = working_database.cursor()
    state = sys.argv[4]
    query = f"SELECT cities.name FROM cities LEFT JOIN states ON cities.state_id=\
        states.id WHERE states.name='{state}' ORDER BY cities.id ASC"
    cur.execute(query)
    if cur:
        print(", ".join(i[0] for i in cur))
    else:
        print()
    working_database.close()
