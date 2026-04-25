import re

# r = re.match("in","sun rises in east")
# r = re.search("in","sun rises in in east")
# r = re.findall("in","sun in rises in east")
# r = re.finditer("in","sun in rises in east")
# print(next(r))
# print(next(r))

# r = re.sub("s","T","sun rises in east")

# r = re.split("","sun rises in east")
# print(r)



# k = re.findall("s.n","sun rese skn in east")

# k = re.search("^sun","k sun rises in east")
# k = re.search("east$","k sun rises in east")

# k = re.findall("su*n","k sun rises sn suuun in east")
# k = re.findall("su+n","k sauaun rises sn suuun in east")
# k = re.findall("su?n","k sun rises sn suuun in east")

# k = re.findall("[0-9a-z]","k  @ sun rises 898 sn suuun in east 898")
# print(k)


# k = re.findall(r"\d","k sun 89  @$ rises sn suuun 898  in east")

# k = re.findall(r"\D","k sun 89  @$ rises sn suuun 898  in east")


# k = re.findall(r"\W","k sun 89  @$ rises sn suuun 898  in east")


# k = re.findall(r"\S","k sun 89  @$ rises sn suuun 898  in east")


# k = re.findall(r"\Bses","k sun 89  @$ rises sn suuunses 898  in east")
# print(k)


# number = input("enter number : ")
# k = re.match("^[0-9]{10}$",number)
# if k is None:
#     print("Invalid number")
# else:
#     print(number)

email = "chintan@gmail.com"

k = re.match("^[a-z0-9_-]+@[a-z]+\\.[a-z]{2,4}$",email)
print(k)





# ============================================
# PYTHON REGEX (re MODULE) NOTES
# ============================================

import re


# ============================================
# 1. BASIC FUNCTIONS
# ============================================

# r = re.match("in", "sun rises in east")
# → matches only at beginning

# r = re.search("in", "sun rises in east")
# → finds first occurrence anywhere

# r = re.findall("in", "sun in rises in east")
# → returns all matches as list

# r = re.finditer("in", "sun in rises in east")
# → returns iterator of match objects

# print(next(r))
# print(next(r))


# ============================================
# 2. REPLACE & SPLIT
# ============================================

# r = re.sub("s", "T", "sun rises in east")
# → replaces 's' with 'T'

# r = re.split(" ", "sun rises in east")
# print(r)
# → splits string based on pattern


# ============================================
# 3. DOT (.) PATTERN
# ============================================

# k = re.findall("s.n", "sun sen sin son")
# print(k)

# s.n → 's' + any char + 'n'
# matches: sun, sen, sin, son


# ============================================
# 4. START (^) AND END ($)
# ============================================

# k = re.search("^sun", "sun rises in east")
# → must start with 'sun'

# k = re.search("east$", "sun rises in east")
# → must end with 'east'


# ============================================
# 5. QUANTIFIERS (*, +, ?)
# ============================================

# k = re.findall("su*n", "sn sun suuun")
# → * = 0 or more 'u'

# k = re.findall("su+n", "sn sun suuun")
# → + = 1 or more 'u'

# k = re.findall("su?n", "sn sun suun")
# → ? = 0 or 1 'u'


# ============================================
# 6. CHARACTER SETS []
# ============================================

# k = re.findall("[0-9a-z]", "k  @ sun rises 898")
# print(k)

# [0-9] → digits
# [a-z] → lowercase letters


# ============================================
# 7. SPECIAL SEQUENCES
# ============================================

# k = re.findall(r"\d", "abc 123")
# → digits only

# k = re.findall(r"\D", "abc 123")
# → non-digits

# k = re.findall(r"\W", "abc 123 @$")
# → special characters

# k = re.findall(r"\S", "abc 123")
# → non-space characters

# k = re.findall(r"\Bses", "suuunses")
# → not at word boundary


# ============================================
# 8. VALIDATE MOBILE NUMBER
# ============================================

# number = input("Enter number: ")

# k = re.match("^[0-9]{10}$", number)

# if k is None:
#     print("Invalid number")
# else:
#     print("Valid number")


# ============================================
# 9. EMAIL VALIDATION
# ============================================

email = "chintan@gmail.com"

k = re.match("^[a-z0-9_-]+@[a-z]+\\.[a-z]{2,4}$", email)

print(k)


"""
Explanation:

Pattern:
^[a-z0-9_-]+   → username (letters, numbers, _, -)
@              → must have @
[a-z]+         → domain name
\\.            → dot (escaped)
[a-z]{2,4}     → extension (2 to 4 letters)

^ → start of string
$ → end of string

If match found → valid email
Else → invalid
"""


# ============================================
# KEY POINTS
# ============================================

# • re module is used for pattern matching
# • match() → start
# • search() → anywhere
# • findall() → list of matches
# • Regex used in:
#   - validation (email, phone)
#   - search systems
#   - data extraction