# ============================================
# PYTHON DICTIONARY NOTES
# ============================================

# Dictionary:
# - Stores data in Key : Value pairs
# - Mutable (can be modified)
# - Ordered (Python 3.7+)
# - Duplicate keys NOT allowed
# - Duplicate values allowed

# ============================================
# 1. CREATE DICTIONARY
# ============================================

student = {"name": "Mohit", "email": "mohit@gmail.com", "phone": "9876543210"}

print(student)


# ============================================
# 2. ALLOWED KEY TYPES
# ============================================

d = {
    "name": "Yash",  # String Key
    123: "ABC",  # Integer Key
    12.33: "XYZ",  # Float Key
    True: "Hello",  # Boolean Key
    (10, 20, 30): "Tuple",  # Tuple Key
}

print(d)

# NOTE:
# List, Set, and Dictionary cannot be keys
# because they are mutable.


# ============================================
# 3. DUPLICATE KEYS
# ============================================

d = {"name": "Krish", "name": "Yash"}

print(d)

# Output:
# {'name': 'Yash'}

# Last value overwrites previous value.


# ============================================
# 4. ACCESS VALUES
# ============================================

student = {"name": "Mohit", "email": "mohit@gmail.com"}

print(student["name"])
print(student.get("name"))

# Difference:

print(student.get("age"))

# Output:
# None

# student["age"]
# Gives KeyError


# ============================================
# 5. ADD NEW KEY
# ============================================

student["age"] = 25

print(student)


# ============================================
# 6. UPDATE VALUE
# ============================================

student["name"] = "Rahul"

print(student)


# ============================================
# 7. keys()
# ============================================

print(student.keys())

# Output:
# dict_keys(['name', 'email', 'age'])


# ============================================
# 8. values()
# ============================================

print(student.values())

# Output:
# dict_values(['Rahul', 'mohit@gmail.com', 25])


# ============================================
# 9. items()
# ============================================

print(student.items())

# Output:
# dict_items([
# ('name','Rahul'),
# ('email','mohit@gmail.com'),
# ('age',25)
# ])


# ============================================
# 10. LOOPING THROUGH DICTIONARY
# ============================================

for key, value in student.items():
    print(key, value)

# Output:
# name Rahul
# email mohit@gmail.com
# age 25


# ============================================
# 11. update()
# ============================================

student.update({"city": "Surat"})

print(student)

# Adds new key or updates existing key


# ============================================
# 12. pop()
# ============================================

student.pop("age")

print(student)

# Removes specified key


# ============================================
# 13. popitem()
# ============================================

student.popitem()

print(student)

# Removes last inserted item


# ============================================
# 14. clear()
# ============================================

student.clear()

print(student)

# Output:
# {}


# ============================================
# 15. del
# ============================================

student = {"name": "Mohit"}

del student

# Entire dictionary deleted


# ============================================
# 16. COPY DICTIONARY
# ============================================

student = {"name": "Mohit"}

copy1 = student.copy()

copy2 = dict(student)

print(copy1)
print(copy2)


# ============================================
# 17. NESTED DICTIONARY
# ============================================

student = {
    "name": "Mohit",
    "address": {"city": "Surat", "state": "Gujarat", "country": "India"},
}

print(student["address"]["country"])

# Output:
# India


# ============================================
# 18. DICTIONARY WITH LIST
# ============================================

student = {"name": "Mohit", "languages": ["Gujarati", "Hindi", "English"]}

print(student["languages"][0])

# Output:
# Gujarati


# ============================================
# 19. NESTED LOOPING
# ============================================

family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
}

for key, value in family.items():

    print(key)

    for k, v in value.items():
        print(k, v)


# ============================================
# 20. fromkeys()
# ============================================

keys = ("key1", "key2", "key3")

d = dict.fromkeys(keys, 0)

print(d)

# Output:
# {
#   'key1':0,
#   'key2':0,
#   'key3':0
# }


# ============================================
# 21. zip()
# ============================================

keys = ("key1", "key2", "key3")
values = ("abc", "xyz", "pqr")

d = dict(zip(keys, values))

print(d)

# Output:
# {
#   'key1':'abc',
#   'key2':'xyz',
#   'key3':'pqr'
# }


# ============================================
# 22. setdefault()
# ============================================

d = {"subject": "Python", "marks": "123"}

d.setdefault("subject", "Java")

print(d)

# Output:
# {
#   'subject':'Python',
#   'marks':'123'
# }

# Existing key NOT changed


d.setdefault("city", "Surat")

print(d)

# Output:
# {
#   'subject':'Python',
#   'marks':'123',
#   'city':'Surat'
# }

# New key added


# ============================================
# INTERVIEW QUESTIONS
# ============================================

# Q1. Difference between get() and [] ?

# get()
# Returns None if key not found

# []
# Raises KeyError if key not found


# Q2. Can a dictionary have duplicate keys?

# No
# Last value overwrites previous value


# Q3. Can list be a dictionary key?

# No
# Because list is mutable


# Q4. Which data types can be keys?

# String
# Integer
# Float
# Boolean
# Tuple


# Q5. Difference between update() and setdefault() ?

# update()
# Always updates value

# setdefault()
# Adds only if key doesn't exist


# Q6. Is dictionary ordered?

# Yes (Python 3.7+)


# Q7. Is dictionary mutable?

# Yes
