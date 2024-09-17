#!/home/habeeb/venv/bin/python3
"""Module to query a database and print all
    data in the database
"""
#import MySQLdb
from sys import argv
from MySQLdb import connect

# Connecting to the database
conn = connect(host="localhost", port=3306, user=argv[1], password=argv[2], database=argv[3])

# Querying the database
conn.query("""SELECT id, name FROM states ORDER BY states.id""")

# Storing/collecting the address of the result
result = conn.store_result()

# Fetching database from the address
vals = result.fetch_row(maxrows=0)

# Checking if module was imported
if __name__ == "__main__":
    # Then print
    for row in vals:
        print(row)
    # Close the connection
    conn.close()
