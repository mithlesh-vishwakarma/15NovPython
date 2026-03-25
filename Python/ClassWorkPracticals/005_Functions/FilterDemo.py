# ============================================
# PYTHON filter() FUNCTION NOTES
# ============================================


# ============================================
# 1. USING NORMAL FUNCTION WITH LOOP
# ============================================

l = [4, 5, 7, 8, 9, 40, 6, 13, 17]
c = []


def checkeven(a):
    if a % 2 == 0:
        return a  # return value if condition is True


for i in l:
    k = checkeven(i)
    if k is not None:  # only append valid values
        c.append(k)

print(c)  # Output: [4, 8, 40, 6]


# ============================================
# 2. USING filter() FUNCTION
# ============================================

# filter(function, iterable)

# c = filter(checkeven, l)   # using normal function

c = filter(lambda k: k % 2 == 0, l)  # using lambda
print(list(c))  # Output: [4, 8, 40, 6]


# ============================================
# 3. FILTERING STRINGS
# ============================================

sub = ["python", "php", "java", "node", "android"]

k = filter(lambda x: "a" in x, sub)
print(list(k))  # Output: ['java', 'android']


# ============================================
# 4. FILTER USING math MODULE
# ============================================

import math

l = [2, 5, 9, 8, 25, 49, 45, 81, 144, 22, 33]


def sqrt_check(a):
    k = math.sqrt(a)  # find square root
    if k.is_integer():  # check if result is whole number
        return a  # return original number


k = filter(sqrt_check, l)
print(list(k))  # Output: [9, 25, 49, 81, 144]


# USING LAMBDA

k = filter(lambda a: math.sqrt(a).is_integer(), l)
print(list(k))


# ============================================
# KEY POINTS
# ============================================

# • filter() selects elements based on condition
# • Only elements with True condition are returned
# • Returns filter object → convert using list()
# • lambda makes code short and clean

# Difference:

# map() → transforms data
# filter() → selects data
