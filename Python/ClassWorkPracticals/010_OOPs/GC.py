import sys

a= [10,20,30,40,50]

print(sys.getrefcount(a))



# ============================================
# PYTHON MEMORY MANAGEMENT - REFERENCE COUNTING
# ============================================

import sys


# ============================================
# 1. LIST CREATION
# ============================================

a = [10, 20, 30, 40, 50]


# ============================================
# 2. CHECK REFERENCE COUNT
# ============================================

print(sys.getrefcount(a))


"""
Explanation:

sys.getrefcount(object)
→ Returns number of references to that object

Reference = how many variables/places are pointing to the same object
"""


# ============================================
# IMPORTANT NOTE
# ============================================

# Output will be +1 more than expected

# Why?
# Because:
# • When we pass 'a' into getrefcount(), it creates a temporary reference

# Example:
# If actual references = 1
# Output = 2


# ============================================
# 3. INCREASING REFERENCE COUNT
# ============================================

b = a
c = a

print(sys.getrefcount(a))


"""
Explanation:

Now:
a → list
b → points to same list
c → points to same list

So reference count increases

More variables → more references
"""


# ============================================
# 4. DECREASING REFERENCE COUNT
# ============================================

del b

print(sys.getrefcount(a))


"""
Explanation:

del b → removes one reference

If reference count becomes 0:
→ Python automatically deletes object (Garbage Collection)
"""


# ============================================
# KEY POINTS
# ============================================

# • Python uses reference counting for memory management
# • More references → object stays in memory
# • Zero references → object is deleted

# Garbage Collection:
# → Automatically frees unused memory


# ============================================
# REAL-WORLD IMPORTANCE
# ============================================

# • Prevent memory leaks
# • Optimize performance
# • Important in large applications (backend, APIs, ML)