# ============================================
# PYTHON TUPLES - COMPLETE NOTES
# ============================================


# ============================================
# 1. CREATING TUPLE
# ============================================

t = (10, 32, 60, 59, 45, "meet", "A", 45.66, True)
print(t)
print(type(t))
print(len(t))

t = tuple((10, 20, 30))
print(t)


"""
Explanation:

Tuple → Ordered, immutable collection.

• Cannot modify after creation
• Allows different data types
• Allows duplicate values

Defined using () or tuple()
"""


# ============================================
# 2. SINGLE ELEMENT TUPLE
# ============================================

l = [10]
print(type(l))

t = (10,)
print(type(t))

t = tuple((10,))
print(type(t))


"""
Explanation:

(10) → Not a tuple, it's an integer
(10,) → Tuple with one element

Comma is required for single element tuple.
"""


# ============================================
# 3. INDEXING & SLICING
# ============================================

t = (10, 32, 60, 59, 45, "meet", "A", 45.66, True)

print(t[0])
print(t[2:5])
print(t[-5])
print(t[::-1])


"""
Explanation:

Indexing → Access elements using index

Slicing:
tuple[start:end:step]

t[::-1] → Reverse tuple
"""


# ============================================
# 4. LOOPING THROUGH TUPLE
# ============================================

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])


"""
Explanation:

You can loop through tuple like list.

Two methods:
• Direct loop
• Index-based loop
"""


# ============================================
# 5. MODIFY TUPLE (INDIRECT METHOD)
# ============================================

l = list(t)
l.append(500)

t = tuple(l)
print(t)


"""
Explanation:

Tuple is immutable → Cannot change directly.

Workaround:
1. Convert to list
2. Modify
3. Convert back to tuple
"""


# ============================================
# 6. UNPACKING TUPLE
# ============================================

t = (10, 32, 60, 59, 45, "meet", "A", 45.66, True)

(*a, b, c, d) = t

print(a)
print(b)
print(c)
print(d)


"""
Explanation:

Unpacking → Assign values to variables.

*a → Takes multiple values as list
b, c, d → Take last elements

Useful when number of elements is unknown.
"""


# ============================================
# 7. CONCATENATION & REPETITION
# ============================================

t1 = (10, 20, 30)
t2 = (40, 50, 60)

t3 = t1 + t2
print(t3)

print(t3 * 2)


"""
Explanation:

+ → Combines tuples
* → Repeats tuple

Example:
(1,2) * 2 → (1,2,1,2)
"""
