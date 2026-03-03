# ============================================
# PYTHON CONDITIONAL & LOOPING STATEMENTS NOTES
# ============================================


# ============================================
# 1. SIMPLE IF-ELSE CONDITION
# ============================================

age = 19

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")


"""
Explanation:

if → Executes block when condition is True
else → Executes block when condition is False

Syntax:
if condition:
    statement
else:
    statement
"""


# ============================================
# 2. NESTED IF (IF INSIDE IF)
# ============================================

a = 1000
b = 1000
c = 1000

if a > b:
    if a > c:
        print("A is greater")
    else:
        print("C is greater")
else:
    if b > c:
        print("B is greater")
    else:
        print("C is greater")


"""
Explanation:

Nested if → One if statement inside another.

Used when checking multiple related conditions.
"""


# ============================================
# 3. IF-ELIF-ELSE (MULTIPLE CONDITIONS)
# ============================================

if a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
elif c > a and c > b:
    print("C is greater")
else:
    print("All are equal or something went wrong")


"""
Explanation:

elif → Else if (used to check multiple conditions)
Only one block executes.

and → Both conditions must be True
"""


# ============================================
# 4. GRADE SYSTEM PROGRAM
# ============================================

marks = 50

if marks > 90 and marks <= 100:
    print("Grade A")
elif marks > 70 and marks <= 90:
    print("Grade B")
elif marks > 50 and marks <= 70:
    print("Grade C")
elif marks > 34 and marks <= 50:
    print("Grade D")
elif marks >= 0 and marks <= 34:
    print("Grade F")
else:
    print("Invalid marks")


"""
Explanation:

Conditions are checked from top to bottom.

If none match, else block runs.

Always validate range properly in such programs.
"""


# ============================================
# 5. MATCH-CASE (Switch Statement in Python 3.10+)
# ============================================

choice = 2

match choice:
    case 1:
        print("Gujarati")
    case 2:
        print("Hindi")
    case 3:
        print("English")
    case _:
        print("Invalid input")


"""
Explanation:

match-case → Similar to switch statement in other languages.

case _ → Default case (if no match found)

Available in Python 3.10 and above.
"""


# ============================================
# 6. FOR LOOP
# ============================================

for i in range(10):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 1, -1):
    print(i)


"""
Explanation:

for loop → Used for fixed number of iterations.

range(start, stop, step)

range(10)        → 0 to 9
range(3,10)      → 3 to 9
range(1,10,2)    → Step of 2
range(10,1,-1)   → Reverse loop
"""


# ============================================
# 7. WHILE LOOP
# ============================================

i = 0
while i < 5:
    print(i)
    i += 1


"""
Explanation:

while loop → Runs as long as condition is True.

Important:
Make sure to update variable inside loop,
otherwise it may cause infinite loop.
"""


# ============================================
# 8. CONTINUOUS PROGRAM USING WHILE LOOP
# ============================================

choice = 'y'

while choice != 'n':
    marks = int(input("Enter marks: "))

    if marks > 90 and marks <= 100:
        print("Grade A")
    elif marks > 70 and marks <= 90:
        print("Grade B")
    elif marks > 50 and marks <= 70:
        print("Grade C")
    elif marks > 34 and marks <= 50:
        print("Grade D")
    elif marks >= 0 and marks <= 34:
        print("Grade F")
    else:
        print("Invalid marks")

    choice = input("Do you want to continue? y or n: ")


"""
Explanation:

This loop runs until user enters 'n'.

Used for menu-driven programs.

Flow:
1. Ask input
2. Check condition
3. Ask user if continue
4. Repeat until user stops
"""


#control : break, continue, pass

# for i in range(20):  
#     if i==5:
#         # break
#         # continue
#         pass
#     print(i)
