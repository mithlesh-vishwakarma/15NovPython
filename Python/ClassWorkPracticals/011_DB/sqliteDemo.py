# ============================================
# PYTHON SQLITE DATABASE NOTES
# ============================================

import sqlite3


# ============================================
# 1. CONNECT DATABASE
# ============================================

con = sqlite3.connect("data.db")   # creates file if not exists


# ============================================
# 2. CREATE TABLE
# ============================================

# qry = "CREATE TABLE student(id INT, name VARCHAR(20), email VARCHAR(20))"

# con.execute(qry)
# con.commit()


# commit() → saves changes permanently


# ============================================
# 3. INSERT DATA
# ============================================

# qry = "INSERT INTO student VALUES(3, 'Priyanshu', 'sufi@gmail.com')"

# con.execute(qry)
# con.commit()


# ============================================
# 4. UPDATE DATA
# ============================================

# qry = "UPDATE student SET name='sf' WHERE id=2"

# con.execute(qry)
# con.commit()


# ============================================
# 5. DELETE DATA
# ============================================

# qry = "DELETE FROM student WHERE id=1"

# con.execute(qry)
# con.commit()


# ============================================
# 6. FETCH DATA (SELECT)
# ============================================

# data = con.execute("SELECT * FROM student").fetchall()
data = con.execute("SELECT * FROM student")
print(data)


# fetchall() → returns all rows as list of tuples

# Example Output:
# [(1, 'abc', 'abc@gmail.com'), (2, 'xyz', 'xyz@gmail.com')]


# ============================================
# 7. CLOSE CONNECTION
# ============================================

con.close()


# ============================================
# KEY POINTS
# ============================================

# • sqlite3 → built-in database in Python
# • connect() → creates/opens database file
# • execute() → runs SQL query
# • commit() → saves changes
# • fetchall() → gets all records
# • close() → closes connection


# ============================================
# IMPORTANT BEST PRACTICE
# ============================================

# Use parameterized query (avoid SQL injection)

# qry = "INSERT INTO student VALUES(?, ?, ?)"
# con.execute(qry, (4, "Rahul", "rahul@gmail.com"))
# con.commit()


# ============================================
# REAL USE CASE
# ============================================

# • Store user data
# • Login systems
# • Inventory systems
# • Your future dashboard / ERP project