# ============================================
# PYTHON EXCEPTIONS (ERROR TYPES) NOTES
# ============================================


# ============================================
# 1. ValueError
# ============================================

# a = "xcxxc"
# b = int(a)   # ❌ cannot convert string to integer
# print(b)

# ValueError:
# Occurs when correct type is used but invalid value is given


# ============================================
# 2. IndexError
# ============================================

# a = [10, 20, 30]
# print(a[4])   # ❌ index out of range

# IndexError:
# Occurs when accessing invalid index in list/tuple


# ============================================
# 3. KeyError
# ============================================

# d = {"name": "abc"}
# print(d['nam1'])   # ❌ key does not exist

# KeyError:
# Occurs when accessing non-existing key in dictionary


# ============================================
# 4. FileNotFoundError
# ============================================

# f = open("abc.txt", 'r')   # ❌ file not found

# FileNotFoundError:
# Occurs when file does not exist


# ============================================
# 5. TypeError
# ============================================

# a = 10 + "ddds"   # ❌ int + string not allowed

# TypeError:
# Occurs when operation is applied to incompatible types


# ============================================
# 6. AttributeError
# ============================================

# class Demo:
#     pass

# d = Demo()
# print(d.k)   # ❌ attribute does not exist

# AttributeError:
# Occurs when object does not have requested attribute


# ============================================
# 7. NameError
# ============================================

# print(k)   # ❌ variable not defined

# NameError:
# Occurs when variable is not defined


# ============================================
# KEY POINTS
# ============================================

# • Errors are also called Exceptions
# • They stop program execution
# • Important for debugging

# Common Errors:
# ValueError, IndexError, KeyError, TypeError, NameError, etc.


# ============================================
# BONUS: TRY-EXCEPT (HANDLING ERRORS)
# ============================================

try:
    a = int("abc")   # error
except ValueError:
    print("Invalid input")


# try → code that may cause error
# except → handles the error