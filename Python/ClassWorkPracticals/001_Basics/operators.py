# ============================================
# PYTHON OPERATORS - COMPLETE PRACTICE NOTES
# ============================================


# ============================================
# 1. ARITHMETIC OPERATORS
# +, -, *, /, %, **, //
# ============================================

print(10 + 10)
print("abc" + "abc")
# print("10" + 10)   # ❌ Error (string + int not allowed)
print(True + True)
print(False + False)

print(True + 1)
print(True - True)

print(10 * 10)
print("a" * 10)

print(10 // 3)
print(10 % 30)

# print(10 / 0)   # ❌ ZeroDivisionError

print(10 ** 2)


"""
Explanation:

+   → Addition
-   → Subtraction
*   → Multiplication
/   → Division (returns float)
//  → Floor division (removes decimal part)
%   → Modulus (remainder)
**  → Power

Important Concepts:

• "abc" + "abc" → String concatenation
• "a" * 10 → Repeats string 10 times
• True = 1, False = 0 in numeric operations
• Division by zero gives error
"""


# ============================================
# 2. ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=, %=, **=, //=
# ============================================

a = 10

a += 20
a -= 5
a *= 2
a /= 5
a %= 3
a **= 2
a //= 3

print(a)


"""
Explanation:

=    → Assign value
+=   → Add and assign
-=   → Subtract and assign
*=   → Multiply and assign
/=   → Divide and assign
%=   → Modulus and assign
**=  → Power and assign
//=  → Floor divide and assign

These are shortcut operators.
Example:
a += 20  →  a = a + 20
"""


# ============================================
# 3. LOGICAL OPERATORS
# and, or, not
# ============================================

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or False)
print(False or False)

print(not True)


"""
Explanation:

and → True only if both conditions are True
or  → True if at least one condition is True
not → Reverses the boolean value
"""


# ============================================
# 4. COMPARISON (RELATIONAL) OPERATORS
# ==, !=, >, <, >=, <=
# ============================================

a = 10
b = 20
c = 10

print(a == b)
print(a != c)
print(a >= b)
print(a >= c)


"""
Explanation:

==  → Equal to
!=  → Not equal to
>   → Greater than
<   → Less than
>=  → Greater than or equal to
<=  → Less than or equal to

Comparison operators return True or False.
"""


# ============================================
# 5. IDENTITY OPERATORS
# is, is not
# ============================================

a = [10, 20, 30]
b = [10, 20, 30]
c = a

print(a is c)
print(a is b)


"""
Explanation:

is      → Checks if both variables refer to same memory location
is not  → Checks if they refer to different memory locations

Important:
a == b  → Checks values
a is b  → Checks memory reference
"""


# ============================================
# 6. MEMBERSHIP OPERATORS
# in, not in
# ============================================

a = [10, 20, 30, 40]

print(10 in a)
print(100 not in a)


"""
Explanation:

in       → Returns True if value exists in sequence
not in   → Returns True if value does NOT exist

Works with:
list, tuple, string, set, dictionary
"""