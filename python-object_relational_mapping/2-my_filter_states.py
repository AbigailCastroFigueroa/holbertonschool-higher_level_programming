#!/usr/bin/python3
"""Script to filter by a given condition."""
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
    sel_state = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name='{}'\
                COLLATE utf8mb4_bin ORDER BY id ASC;".format(sel_state))
    for i in cur:
        print(i)
    working_database.close()
