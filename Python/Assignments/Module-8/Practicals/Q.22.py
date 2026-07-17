# Q.22 Write a Python program to insert data into an SQLite3 database and fetch it

import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Adding IF NOT EXISTS logic handled in Q.21, here we just insert
try:
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    conn.commit()
except sqlite3.OperationalError:
    print("Make sure to run Q.21.py first to create the table!")

try:
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("Fetched Data:")
    for row in rows:
        print(row)
except sqlite3.OperationalError:
    pass

conn.close()
