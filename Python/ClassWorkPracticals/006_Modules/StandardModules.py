# ============================================
# PYTHON BUILT-IN MODULES NOTES
# ============================================


# ============================================
# 1. MATH MODULE
# ============================================

import math

print(math.pi)          # Value of PI → 3.14159...
print(math.sqrt(25))    # Square root → 5.0
print(math.floor(45.56))# Round down → 45
print(math.ceil(45.0001)) # Round up → 46
print(round(45.55))     # Round to nearest → 46


"""
Explanation:

math module → Used for mathematical operations

pi        → Constant value
sqrt()    → Square root
floor()   → Smallest integer
ceil()    → Largest integer
round()   → Nearest integer
"""


# ============================================
# 2. OS MODULE (OPERATING SYSTEM)
# ============================================

import os

# os.mkdir("NEW FOLDER")   # Create folder
# os.rmdir("NEW FOLDER")   # Delete folder


"""
Explanation:

os module → Interact with operating system

mkdir() → Create directory
rmdir() → Remove directory (must be empty)
"""


# ============================================
# 3. SYS MODULE
# ============================================

import sys

print(sys.path)              # Python module search paths
# print(sys.getwindowsversion())  # Windows version (works only on Windows)


"""
Explanation:

sys module → System-specific parameters

sys.path → Shows paths where Python looks for modules
"""


# ============================================
# 4. DATETIME MODULE
# ============================================

import datetime

dt = datetime.datetime.now()

print(dt.date())   # Current date


"""
Explanation:

datetime module → Work with date and time

now() → Current date & time
date() → Extract only date
"""


# ============================================
# 5. CALENDAR MODULE
# ============================================

import calendar

print(calendar.month(2030, 12))


"""
Explanation:

calendar module → Work with calendar data

month(year, month) → Displays calendar of given month
"""


# ============================================
# 6. RANDOM MODULE
# ============================================

import random

r = random.randint(100, 999)
print(r)


"""
Explanation:

random module → Generate random values

randint(a, b) → Random number between a and b (inclusive)

Used in:
• OTP generation
• Games
• Testing
"""
