# class Demo:

#     name = "krish"
#     def __init__(self):
#         print("Demo calling")

#     def __str__(self):
#         return self.name

# d =  Demo()
# print(d)



# class Calc:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __eq__(self, value):
#         return self.a==value.a and self.b==value.b

# c1 = Calc(10,20)
# c2 = Calc(10,20)
# print(c1==c2)



class Sample:

    def __init__(self,a):
        self.a = a

    def __len__(self):
        return len(self.a)
    
    def __getitem__(self, key):
        return self.a[key]

    def __setitem__(self, key, value):
        self.a[key] = value
        


s = Sample([10,20,30,40,50])
# print(len(s))
s[1] = 1000
print(s[1])


# ============================================
# PYTHON MAGIC METHODS (DUNDER METHODS) NOTES
# ============================================


# ============================================
# 1. __str__ METHOD (STRING REPRESENTATION)
# ============================================

class Demo:

    name = "krish"

    def __init__(self):
        print("Demo calling")

    def __str__(self):
        return self.name   # what to print when object is printed


d = Demo()
print(d)   # Output: krish


# Explanation:
# __str__ → controls what gets printed when using print(object)
# Instead of memory address, it shows custom value


# ============================================
# 2. __eq__ METHOD (EQUALITY COMPARISON)
# ============================================

class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, value):
        return self.a == value.a and self.b == value.b


c1 = Calc(10, 20)
c2 = Calc(10, 20)

print(c1 == c2)   # Output: True


# Explanation:
# __eq__ → defines behavior of '==' operator
# Without this, objects compare memory addresses
# With this, compares actual values


# ============================================
# 3. __len__, __getitem__, __setitem__
# ============================================

class Sample:

    def __init__(self, a):
        self.a = a   # storing list

    def __len__(self):
        return len(self.a)   # allows len(object)

    def __getitem__(self, key):
        return self.a[key]   # allows indexing → object[index]

    def __setitem__(self, key, value):
        self.a[key] = value  # allows assignment → object[index] = value


s = Sample([10, 20, 30, 40, 50])

print(len(s))   # Output: 5

s[1] = 1000     # uses __setitem__
print(s[1])     # uses __getitem__ → Output: 1000


# ============================================
# KEY POINTS
# ============================================

# • Magic methods start and end with __ (dunder methods)
# • Used to customize built-in operations
# • Makes objects behave like built-in types (list, string, etc.)


# ============================================
# COMMON MAGIC METHODS
# ============================================

# __init__     → constructor
# __str__      → string representation
# __eq__       → equality check
# __len__      → length
# __getitem__  → access by index
# __setitem__  → assign value
# __add__      → + operator
# __sub__      → - operator


# ============================================
# REAL-WORLD USE CASE
# ============================================

# • Custom data structures
# • Frameworks (Django, Flask internally use this)
# • Making objects behave like lists/dictionaries