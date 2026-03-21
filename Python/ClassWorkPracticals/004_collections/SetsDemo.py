# ============================================
# PYTHON SETS - COMPLETE NOTES
# ============================================


# ============================================
# 1. CREATING SET
# ============================================

s = {10, 20, 30, 40, 50, 50, 1, True, False, 0}
print(s)
print(type(s))
print(len(s))

s = {10}
print(s)
print(type(s))

l = set()
print(type(l))


"""
Explanation:

Set → Unordered, mutable collection of unique elements.

Important Points:
• Duplicate values are automatically removed
• True = 1 and False = 0 (so duplicates may be removed)

{} → Creates set
set() → Creates empty set (important, {} creates dict)

Example:
{10,20,30,30} → {10,20,30}
"""


# ============================================
# 2. LOOPING & MEMBERSHIP
# ============================================

s = {10, 20, 30, 40, 50, 60}

for i in s:
    print(i)

print(10 in s)


"""
Explanation:

for loop → Used to iterate set elements

in → Checks if value exists in set
Returns True or False
"""


# ============================================
# 3. ADD & REMOVE ELEMENTS
# ============================================

s.add(800)
print(s)

# s.remove(100)   # ❌ Error if element not found
s.discard(100)  # ✔ Safe (no error if not found)
print(s)

s.pop()
print(s)


"""
Explanation:

add() → Adds element

remove() → Removes element (error if not present)
discard() → Removes safely (no error)

pop() → Removes random element (since set is unordered)
"""


# ============================================
# 4. CLEAR & DELETE
# ============================================

# s.clear()   → Removes all elements
# del s       → Deletes entire set


"""
Explanation:

clear() → Makes set empty
del → Deletes set from memory
"""


# ============================================
# 5. SET OPERATIONS
# ============================================

a = {10, 20, 30, 40, 50, True}
b = {40, 50, 60, 70, 80, 1}

# UNION
c = a.union(b)
c = a | b
print(c)

# INTERSECTION
c = a.intersection(b)
c = a & b
print(c)

# DIFFERENCE
c = a.difference(b)
c = b - a
print(c)

# SYMMETRIC DIFFERENCE
c = a.symmetric_difference(b)
c = a ^ b
print(c)


"""
Explanation:

Union (|) → All elements from both sets
Intersection (&) → Common elements
Difference (-) → Elements in one but not in other
Symmetric Difference (^) → Elements not common
"""


# ============================================
# 6. UPDATE OPERATIONS
# ============================================

a = {10, 20, 30}
b = {30, 40, 50}

a.update(b)
print(a)


"""
Explanation:

update() → Adds all elements of another set into current set
(Original set changes)
"""


# ============================================
# 7. FROZENSET
# ============================================

k = frozenset({10, 20, 30})
print(k)


"""
Explanation:

frozenset → Immutable version of set

• Cannot add/remove elements
• Used when data should not change
"""


# ============================================
# 8. COPY SET
# ============================================

k = a.copy()
print(k)


"""
Explanation:

copy() → Creates new set with same elements
"""


# ============================================
# 9. SET RELATION METHODS
# ============================================

a = {10, 20, 30, 40}
b = {100, 500}

print(b.issubset(a))
print(a.issuperset(b))
print(a.isdisjoint(b))


"""
Explanation:

issubset() → Checks if all elements of one set are in another
issuperset() → Opposite of subset
isdisjoint() → True if no common elements
"""
