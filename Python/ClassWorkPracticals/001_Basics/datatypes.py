# ============================================
# PYTHON DATA TYPES - PRACTICE NOTES
# ============================================


# ============================================
# 1. NUMERIC DATA TYPES
# int, float, complex
# ============================================

a = 10
print(type(a))

b = 10.565
print(type(b))

c = 4 + 5j
print(type(c))


"""
Explanation:

int     → Integer numbers (whole numbers)
float   → Decimal numbers
complex → Numbers with imaginary part (j)

Example:
10        → int
10.565    → float
4 + 5j    → complex
"""


# ============================================
# 2. SEQUENCE DATA TYPES
# str, list, tuple, range
# ============================================

name = "krish"
print(type(name))

l = [10, 20, 30, 40]
print(type(l))

t = (10, 20, 30, 40)
print(type(t))

k = range(1, 10)
print(type(k))


"""
Explanation:

str   → String (text data) - written inside quotes
list  → Ordered collection, mutable (can change values)
tuple → Ordered collection, immutable (cannot change values)
range → Generates sequence of numbers

Examples:
"krish"          → string
[10,20,30,40]    → list
(10,20,30,40)    → tuple
range(1,10)      → numbers from 1 to 9
"""


# ============================================
# 3. MAPPING DATA TYPE
# dict
# ============================================

st = {"name": "Manish", "email": "manish@gmail.com"}
print(type(st))


"""
Explanation:

dict → Dictionary stores data in key:value pairs

Structure:
{
   "key": "value"
}

Example:
"name"  → key
"Manish" → value
"""


# ============================================
# 4. SET DATA TYPE
# set
# ============================================

s = {10, 20, 30, 40}
print(type(s))


"""
Explanation:

set → Unordered collection of unique elements

Important:
• No duplicate values allowed
• No indexing
• Elements are unique
"""


# ============================================
# 5. BOOLEAN DATA TYPE
# bool
# ============================================

a = True
print(type(a))


"""
Explanation:

bool → Boolean type
Only two values:
True
False

Used in conditions and comparisons.
"""


# ============================================
# 6. TYPE CASTING (Type Conversion)
# ============================================

a = "10"
b = int(a)

print(type(a))
print(type(b))


"""
Explanation:

Type casting means converting one data type into another.

int()    → Convert to integer
float()  → Convert to float
str()    → Convert to string
bool()   → Convert to boolean

Important:
You can only convert compatible values.

Example:
"10" → int("10")  ✔ valid
"hello" → int("hello")  ✘ error
"""