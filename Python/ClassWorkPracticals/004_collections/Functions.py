# ============================================
# PYTHON FUNCTIONS - COMPLETE NOTES
# ============================================


# ============================================
# 1. SIMPLE FUNCTION
# ============================================


def test():
    print("Test calling")


test()


"""
Explanation:

Function → Block of code that runs when called.

def → Keyword to define function

test() → Function call
"""


# ============================================
# 2. FUNCTION WITH PARAMETERS
# ============================================


def square(a):
    sq = a * a
    print(f"square of {a} is {sq}")


square(11)
square(15)


"""
Explanation:

Parameter → Input to function

a → Parameter
11, 15 → Arguments

Function can take input and perform operations.
"""


# ============================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================


def add(a, b):
    r = a + b
    print(f"addition of {a} and {b} is {r}")


add(10, 20)


"""
Explanation:

Function can accept multiple inputs.

a, b → Parameters
"""


# ============================================
# 4. FUNCTION WITH RETURN VALUE
# ============================================


def mul(a, b):
    r = a * b
    return r


r = mul(10, 20)
print(r)

print(mul(50, 40))


"""
Explanation:

return → Sends result back to caller

Difference:
print() → Shows output
return → Gives value for further use
"""


# ============================================
# 5. DEFAULT PARAMETERS
# ============================================


def person(name="ddds", email="fdf", phone=1213132132):
    print(name, email, phone)


person("manish", phone=889898989)


"""
Explanation:

Default values are used if no argument is passed.

You can override specific values using keyword arguments.
"""


# ============================================
# 6. *args (MULTIPLE POSITIONAL ARGUMENTS)
# ============================================


def add(*a):
    print(a)


add(10, 20, 30, 40, 50, 60)


"""
Explanation:

*args → Accepts multiple values

All values are stored as tuple.

Useful when number of inputs is unknown.
"""


# ============================================
# 7. **kwargs (MULTIPLE KEYWORD ARGUMENTS)
# ============================================


def person(**a):
    print(a)


person(name="abc", email="abc@gmail.com")


"""
Explanation:

**kwargs → Accepts multiple key-value arguments

Stored as dictionary.
"""


# ============================================
# 8. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================

k = lambda a, b: a + b
print(k(10, 20))

k = lambda a: a * a
print(k(5))


"""
Explanation:

lambda → Short function without name

Syntax:
lambda parameters : expression

Used for small, one-line functions.
"""
