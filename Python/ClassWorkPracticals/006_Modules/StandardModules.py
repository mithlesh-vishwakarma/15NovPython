# ============================================
# PYTHON BUILT-IN MODULES NOTES
# ============================================


# ============================================
# 1. MATH MODULE
# ============================================

import math

<<<<<<< HEAD
print(math.pi)  # 3.14159... → Value of PI
print(math.sqrt(25))  # 5.0 → Square root
print(math.floor(45.56))  # 45 → Round down to nearest integer
print(math.ceil(45.0001))  # 46 → Round up to nearest integer
print(round(45.55))  # 46 → Round to nearest value


# math module is used for:
# • mathematical calculations
# • scientific computations
=======
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
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36


# ============================================
# 2. OS MODULE (OPERATING SYSTEM)
# ============================================

import os

<<<<<<< HEAD
# os.mkdir("NEW FOLDER")   # Create a new folder
# os.rmdir("NEW FOLDER")   # Remove folder (must be empty)


# os module is used for:
# • file and folder operations
# • interacting with system
=======
# os.mkdir("NEW FOLDER")   # Create folder
# os.rmdir("NEW FOLDER")   # Delete folder


"""
Explanation:

os module → Interact with operating system

mkdir() → Create directory
rmdir() → Remove directory (must be empty)
"""
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36


# ============================================
# 3. SYS MODULE
# ============================================

import sys

<<<<<<< HEAD
print(sys.path)  # Shows paths where Python searches modules
# print(sys.getwindowsversion())  # Works only on Windows


# sys module is used for:
# • system-level operations
# • accessing interpreter details
=======
print(sys.path)              # Python module search paths
# print(sys.getwindowsversion())  # Windows version (works only on Windows)


"""
Explanation:

sys module → System-specific parameters

sys.path → Shows paths where Python looks for modules
"""
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36


# ============================================
# 4. DATETIME MODULE
# ============================================

import datetime

dt = datetime.datetime.now()

<<<<<<< HEAD
print(dt.date())  # Current date


# datetime module is used for:
# • working with date and time
# • getting current timestamp
=======
print(dt.date())   # Current date


"""
Explanation:

datetime module → Work with date and time

now() → Current date & time
date() → Extract only date
"""
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36


# ============================================
# 5. CALENDAR MODULE
# ============================================

import calendar

<<<<<<< HEAD
print(calendar.month(2030, 12))  # Shows December 2030 calendar


# calendar module is used for:
# • displaying calendar
# • date-related operations
=======
print(calendar.month(2030, 12))


"""
Explanation:

calendar module → Work with calendar data

month(year, month) → Displays calendar of given month
"""
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36


# ============================================
# 6. RANDOM MODULE
# ============================================

import random

r = random.randint(100, 999)
<<<<<<< HEAD
print(r)  # Random number between 100 and 999


# random module is used for:
# • generating random values
# • OTP, games, testing


# ============================================
# KEY POINTS
# ============================================

# • Modules help extend Python functionality
# • import is used to include module
# • Each module is specialized for specific tasks
=======
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
>>>>>>> 864f4ac8144e6bdde8b250f7d0f5e799be8c6a36
