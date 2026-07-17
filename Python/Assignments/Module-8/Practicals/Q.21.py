# Q.21 Write a Python program to create a database and a table using SQLite3. 

import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

conn.commit()
conn.close()
print("Database and table created successfully.")
