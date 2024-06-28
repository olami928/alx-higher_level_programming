#!/usr/bin/python3
"""
This code ists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    state_name = sys.argv[4]
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE BINARY \
            name = '{}' ORDER BY id ASC".format(state_name))
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
