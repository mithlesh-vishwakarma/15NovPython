# ============================================
# PYTHON BUILT-IN MODULES NOTES
# ============================================


# ============================================
# 1. MATH MODULE
# ============================================

import math

print(math.pi)  # 3.14159... → Value of PI
print(math.sqrt(25))  # 5.0 → Square root
print(math.floor(45.56))  # 45 → Round down to nearest integer
print(math.ceil(45.0001))  # 46 → Round up to nearest integer
print(round(45.55))  # 46 → Round to nearest value


# math module is used for:
# • mathematical calculations
# • scientific computations


# ============================================
# 2. OS MODULE (OPERATING SYSTEM)
# ============================================

import os

# os.mkdir("NEW FOLDER")   # Create a new folder
# os.rmdir("NEW FOLDER")   # Remove folder (must be empty)


# os module is used for:
# • file and folder operations
# • interacting with system


# ============================================
# 3. SYS MODULE
# ============================================

import sys

print(sys.path)  # Shows paths where Python searches modules
# print(sys.getwindowsversion())  # Works only on Windows


# sys module is used for:
# • system-level operations
# • accessing interpreter details


# ============================================
# 4. DATETIME MODULE
# ============================================

import datetime

dt = datetime.datetime.now()

print(dt.date())  # Current date


# datetime module is used for:
# • working with date and time
# • getting current timestamp


# ============================================
# 5. CALENDAR MODULE
# ============================================

import calendar

print(calendar.month(2030, 12))  # Shows December 2030 calendar


# calendar module is used for:
# • displaying calendar
# • date-related operations


# ============================================
# 6. RANDOM MODULE
# ============================================

import random

r = random.randint(100, 999)
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
