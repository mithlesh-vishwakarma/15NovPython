import sqlite3

conn = sqlite3.connect("test.db")


# cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

qry ="INSERT INTO users VALUES ('mithlesh', 27)"
# cursor.execute("INSERT INTO users (name, age) VALUES ('Sufiyan', 26)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Sagar', 25)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Karan', 25)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Krupa', 23
# )")

conn.commit()
conn.close()