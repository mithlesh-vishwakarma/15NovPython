# ============================================
# PYTHON FILE HANDLING & JSON NOTES
# ============================================


# ============================================
# 1. WRITE MODE ('w')
# ============================================

# f = open("test.txt", 'w')
# f.write("This is my first IO practical")
# f.close()


# 'w' mode:
# • Creates file if not exists
# • Overwrites existing content


# ============================================
# 2. READ MODE ('r')
# ============================================

f = open("test.txt", "r")

# data = f.read()        # Reads full file
# data = f.readlines()  # Reads all lines as list


# Reading line by line

# while True:
#     data = f.readline()
#     print(data)
#     if not data:   # stop when file ends
#         break


f.close()


# ============================================
# 3. APPEND MODE ('a')
# ============================================

# f = open("test.txt", 'a')
# f.write("Hello java")
# f.close()


# 'a' mode:
# • Adds data at end of file
# • Does not overwrite existing content


# ============================================
# 4. WRITELINES()
# ============================================

# f = open("test.txt", 'w')
# f.writelines(['Hello python\n', 'Hello java\n', 'Hello php\n'])
# f.close()


# writelines():
# • Writes multiple lines
# • Must add '\n' manually for new lines


# ============================================
# 5. SEARCH IN FILE
# ============================================

# f = open("test.txt", 'r')

# while True:
#     data = f.readline()
#     if 'Hello' in data:
#         print(data)
#     if not data:
#         break

# f.close()


# ============================================
# 6. WITH STATEMENT (BEST PRACTICE)
# ============================================

# with open("test.txt", 'r') as f:
#     data = f.read()
#     print(data)


# with automatically closes file (no need f.close())


# ============================================
# 7. FILE POINTER (seek & tell)
# ============================================

# with open("test.txt", 'r') as f:
#     f.seek(10)         # move cursor to position 10
#     print(f.tell())    # current position

#     data = f.read()
#     print(f.tell())    # position after reading
#     print(data)


# ============================================
# 8. READ + WRITE MODE ('r+')
# ============================================

# with open("home.txt", 'r+') as f:
#     f.write("Hello python")
#     f.seek(0)
#     data = f.read()
#     print(data)


# 'r+' mode:
# • Read and write both
# • Does not delete existing content


# ============================================
# 9. BINARY MODE
# ============================================

# with open('img.jpg', 'rb') as f:
#     data = f.read()
#     print(data)


# 'rb' → Read binary (images, videos, etc.)


# ============================================
# 10. JSON FILE HANDLING
# ============================================

import json

d = {"name": "priyanshu", "email": "priyanshu@gmail.com"}

with open("data.json", "w") as f:
    json.dump(d, f)  # writes dictionary into JSON file


"""
Explanation:

json.dump(data, file)
→ Converts Python dictionary to JSON and stores in file
"""


# ============================================
# EXTRA: READ JSON
# ============================================

# with open("data.json", 'r') as f:
#     data = json.load(f)
#     print(data)


# json.load()
# → Reads JSON file and converts to Python dictionary


# ============================================
# KEY POINTS
# ============================================

# • open() → open file
# • modes → 'r', 'w', 'a', 'r+', 'rb'
# • with → best practice (auto close)
# • seek() → move cursor
# • tell() → current position
# • JSON → used for data storage & APIs
