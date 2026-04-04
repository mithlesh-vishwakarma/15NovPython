# ============================================
# PYTHON ITERATORS & GENERATORS NOTES
# ============================================


# ============================================
# 1. ITERATOR (iter() and next())
# ============================================

l = [10, 20, 30, 40, 50, 60]

it = iter(l)  # Convert list into iterator

print(next(it))  # 10 → first element
print(next(it))  # 20 → second element
print(next(it))  # 30 → third element


# Explanation:

# iter() → converts iterable (list, tuple) into iterator
# next() → gives next value from iterator

# Iterator keeps track of current position


# ============================================
# 2. GENERATOR FUNCTION (yield)
# ============================================


def calc(a):
    for i in range(1, a):
        yield i * i  # returns value one by one


k = calc(10)

print(next(k))  # 1
print(next(k))  # 4
print(next(k))  # 9
print(next(k))  # 16


# ============================================
# GENERATOR EXPLANATION
# ============================================

# yield → works like return, but:
# • pauses function
# • remembers state
# • resumes from same point on next call


# Flow:

# calc(10) creates generator object

# next(k):
# i=1 → 1*1 = 1
# i=2 → 4
# i=3 → 9
# i=4 → 16
# ... continues until i=9


# ============================================
# GENERATOR VS NORMAL FUNCTION
# ============================================

# Normal function:
# → returns all values at once

# Generator:
# → returns values one by one
# → saves memory


# ============================================
# KEY POINTS
# ============================================

# • Iterator → object with next() method
# • Generator → function using yield
# • Generators are memory efficient
# • Useful for large data processing
