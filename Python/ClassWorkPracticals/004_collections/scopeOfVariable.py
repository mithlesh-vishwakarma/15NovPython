# ============================================
# PYTHON VARIABLE SCOPE - GLOBAL KEYWORD
# ============================================

a = 10  # Global variable (defined outside function)


def test():
    global a  # This tells Python: use the global variable 'a'

    a = 20  # Modifying global variable
    print(a)  # Output: 20 (updated value)


print(a)  # Output: 10 (initial global value)

test()  # Function call → modifies global 'a'

print(a)  # Output: 20 (global value changed after function)


# ============================================
# WITHOUT USING GLOBAL (IMPORTANT DIFFERENCE)
# ============================================

a = 10  # Global variable


def test():
    a = 20  # Local variable (inside function only)
    print(a)  # Output: 20 (local value)


print(a)  # Output: 10 (global value)

test()  # Function call

print(a)  # Output: 10 (global value unchanged)


# ============================================
# KEY POINTS
# ============================================

# • Global variable → declared outside function
# • Local variable → declared inside function
# • global keyword → used to modify global variable inside function

# Without 'global':
# → Python creates a new local variable
# → Original global variable remains unchanged
