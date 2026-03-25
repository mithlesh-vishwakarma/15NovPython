# ============================================
# PYTHON reduce() FUNCTION NOTES
# ============================================

from functools import reduce  # reduce is in functools module

# ============================================
# 1. BASIC EXAMPLE - SUM OF LIST
# ============================================

k = [10, 20, 50, 40, 50, 60]

# reduce(function, iterable)

r = reduce(lambda a, b: a + b, k)
print(r)  # Output: 230


"""
Explanation:

reduce() → Applies function cumulatively on elements

Working:
Step 1: a=10, b=20 → 30
Step 2: a=30, b=50 → 80
Step 3: a=80, b=40 → 120
Step 4: a=120, b=50 → 170
Step 5: a=170, b=60 → 230

Final result → 230
"""


# ============================================
# 2. FIND MINIMUM VALUE
# ============================================

r = reduce(lambda a, b: a if a < b else b, k)
print(r)  # Output: 10


"""
Explanation:

This finds smallest number.

Logic:
If a < b → keep a
else → keep b

Step-by-step:
Compare values one by one → keep smallest
"""


# ============================================
# 3. USING NORMAL FUNCTION (ALTERNATIVE)
# ============================================


def add(a, b):
    print(a, b)  # to see how reduce works step by step
    return a + b


r = reduce(add, k)
print(r)


"""
Explanation:

You can use normal function instead of lambda.

This helps in understanding internal working.
"""


# ============================================
# KEY POINTS
# ============================================

# • reduce() reduces list to single value
# • Works cumulatively (step by step)
# • Requires import from functools
# • Used for:
#   - sum
#   - product
#   - max/min
#   - complex calculations

# Difference:

# map()    → transforms each element
# filter() → selects elements
# reduce() → produces single result
