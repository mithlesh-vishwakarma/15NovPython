# ============================================
# PYTHON STRING METHODS & SLICING NOTES
# ============================================


st = "sun rises in East"


# ============================================
# 1. BASIC STRING METHODS
# ============================================

print(len(st))
print(st.lower())
print(st.casefold())
print(st.upper())
print(st.title())
print(st.capitalize())
print(st)
print(st.strip())


"""
Explanation:

len(st)        → Returns length of string (including spaces)
lower()        → Converts all characters to lowercase
casefold()     → Stronger lowercase (used for comparisons)
upper()        → Converts all characters to uppercase
title()        → First letter of each word capitalized
capitalize()   → First letter of entire string capitalized
strip()        → Removes spaces from beginning and end
"""


# ============================================
# 2. MODIFYING STRINGS
# ============================================

print(st.replace('s', 'T', 2))
print(st.find(" "))
print(st.startswith("su"))
print(st.endswith("st"))


"""
Explanation:

replace(old, new, count)
→ Replaces first 'count' occurrences.

find(" ")
→ Returns index position of first match.
If not found, returns -1.

startswith("su")
→ Returns True if string starts with given text.

endswith("st")
→ Returns True if string ends with given text.
"""


# ============================================
# 3. SPLIT & JOIN
# ============================================

print(st.split("s", 2))
print("abc".join("xyz"))


"""
Explanation:

split(separator, maxsplit)
→ Splits string into list.

join()
→ Joins characters using given string.

Example:
"abc".join("xyz")
Output: xabcyabcz
"""


# ============================================
# 4. CHECKING STRING CONTENT
# ============================================

print("abc".isalpha())
print("123sdd".isdigit())
print("qbc".isalnum())


"""
Explanation:

isalpha() → True if only letters
isdigit() → True if only digits
isalnum() → True if letters and numbers only
"""


# ============================================
# 5. STRING FORMATTING METHODS
# ============================================

print("abc".zfill(10))
print("abc".center(16, "*"))


"""
Explanation:

zfill(width)
→ Adds zeros at beginning to make total width.

center(width, char)
→ Centers string and fills sides with given character.
"""


# ============================================
# 6. STRING SLICING
# ============================================

print(st[2:15:2])
print(st[:8])
print(st[-4:-1])
print(st[::-1])


"""
Explanation:

Slicing syntax:
string[start : end : step]

st[2:15:2]
→ From index 2 to 14 with step 2

st[:8]
→ From beginning to index 7

st[-4:-1]
→ Negative indexing (counts from end)

st[::-1]
→ Reverse string
"""