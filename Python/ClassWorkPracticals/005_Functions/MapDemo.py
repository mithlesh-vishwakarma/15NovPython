# ============================================
# PYTHON map() FUNCTION & LAMBDA NOTES
# ============================================


# ============================================
# 1. USING NORMAL FUNCTION WITH LOOP
# ============================================

l = [10, 20, 30, 40, 50]
k = []


def square(a):
    return a * a  # function to calculate square


for i in l:
    sq = square(i)  # calling function
    k.append(sq)  # storing result

print(k)  # Output: [100, 400, 900, 1600, 2500]


# ============================================
# 2. USING map() FUNCTION
# ============================================

# map(function, iterable)

k = map(square, l)  # applies square() to each element
print(list(k))  # convert map object to list


# ============================================
# 3. USING LAMBDA WITH map()
# ============================================

# lambda → short anonymous function

k = map(lambda a: a * a, l)  # square using lambda
print(list(k))


# ============================================
# 4. map() WITH MULTIPLE LISTS
# ============================================

a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

# pow(x, y) → x raised to power y

k = map(lambda x, y: pow(x, y), a, b)
print(list(k))


# ============================================
# 5. USING map() ON STRINGS
# ============================================

sub = ["python", "php", "java", "node", "android"]

k = map(lambda x: len(x), sub)  # find length of each string
print(list(k))


# ============================================
# KEY POINTS
# ============================================

# • map() applies function to each element of iterable
# • Returns a map object → convert using list()
# • lambda is used for short functions
# • Can use multiple iterables in map()

# map() vs loop:
# → map() is shorter and cleaner
# → loop gives more control
