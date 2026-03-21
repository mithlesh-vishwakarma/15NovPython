# ============================================
# PYTHON RECURSION - FUNCTION CALLING ITSELF
# ============================================


def square(a):
    print(a * a)
    a += 1
    if a <= 10:
        square(a)


square(1)


"""
Explanation:

Recursion → A function calling itself.

Here:
square() function calls itself again and again
until the condition becomes False.


Step-by-step flow:

square(1)
→ prints 1*1 = 1
→ calls square(2)

square(2)
→ prints 4
→ calls square(3)

...

square(10)
→ prints 100
→ a becomes 11
→ condition fails → recursion stops


Important Concept:

Base Condition (Stopping Condition):
if a <= 10

Without this condition, recursion will run infinitely
and cause error (RecursionError).


Key Points:

• Function must have stopping condition
• Each call moves toward stopping condition
• Used in problems like:
  - factorial
  - fibonacci
  - tree traversal
"""
