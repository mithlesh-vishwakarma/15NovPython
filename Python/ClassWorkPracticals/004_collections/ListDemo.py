# ============================================
# PYTHON LISTS - COMPLETE NOTES
# ============================================


# ============================================
# 1. CREATING LIST
# ============================================

l = [100, 200, 300, 400, 100, "abc", True, 45.66]
print(l)
print(len(l))
print(type(l))

l = list((10, 20, 30, 40))
print(l)


"""
Explanation:

List → Ordered, mutable collection.

• Can store different data types
• Allows duplicate values
• Defined using [] or list()

len() → Returns number of elements
type() → Shows datatype
"""


# ============================================
# 2. LIST INDEXING & SLICING
# ============================================

l = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(l[0])
print(l[-2])
print(l[2:5])
print(l[-4:-1])
print(l[1:8:2])
print(l[::-1])


"""
Explanation:

Indexing → Access single element
l[0] → First element
l[-1] → Last element

Slicing:
list[start:end:step]

l[::-1] → Reverse list
"""


# ============================================
# 3. MODIFYING LIST
# ============================================

l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
k = ["a", "b", "c"]

l[0] = 500
l[2:5] = [100, 200, 500, 900]

l.insert(0, 1000)
l.append(1000)
l.append(k)
l.extend(k)

l.remove(10)
l.pop(1)

print(l)


"""
Explanation:

insert(index, value) → Insert at specific position
append(value) → Add single element at end
append(list) → Adds whole list as one element
extend(list) → Adds elements of list individually

remove(value) → Removes first occurrence
pop(index) → Removes element by index
"""


# ============================================
# 4. DELETE OPERATIONS
# ============================================

l.clear()

# del l   # deletes entire list


"""
Explanation:

clear() → Removes all elements (list becomes empty)
del l   → Deletes entire list from memory
"""


# ============================================
# 5. LOOPING THROUGH LIST
# ============================================

l = [10, 20, 30, 40]

for i in l:
    print(i)

for i in range(len(l)):
    print(l[i])

i = 0
while i < len(l):
    print(l[i])
    i += 1


"""
Explanation:

3 ways to loop:

1. Direct loop → for i in list
2. Index loop → range(len(list))
3. While loop → manual control
"""


# ============================================
# 6. LIST COMPREHENSION
# ============================================

sub = ["python", "python", "java", "php", "android", "ios", "react"]

n = [i for i in sub if "a" in i]
print(n)

n = [i for i in sub if i.startswith("p")]
print(n)

n = ["abc" for i in sub]
print(n)


"""
Explanation:

List comprehension → Short way to create lists.

Syntax:
[expression for item in list if condition]

Faster and cleaner than normal loop.
"""


# ============================================
# 7. SORTING LIST
# ============================================

sub.sort(reverse=True)
sub.reverse()

k = sorted(sub)
print(k)


"""
Explanation:

sort() → Sorts original list
reverse=True → Descending order

reverse() → Just reverses list

sorted() → Returns new sorted list (original unchanged)
"""


# ============================================
# 8. COPYING LIST
# ============================================

l = sub
l = sub.copy()
l = list(sub)

print(l)


"""
Explanation:

l = sub → Reference copy (same memory)
copy()  → Creates new list
list()  → Another way to copy list
"""


# ============================================
# 9. COUNT & INDEX
# ============================================

print(sub.count("python"))
print(sub.index("python"))


"""
Explanation:

count(value) → Number of times value appears
index(value) → First occurrence position
"""
