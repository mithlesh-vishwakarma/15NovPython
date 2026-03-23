# Practical Example 7: Write a Python program to calculate grades based on percentage using
# if-else ladder.

# take input
per = float(input("Enter percentage: "))

# check grade
if per >= 90:
    print("Grade: A+")
elif per >= 80:
    print("Grade: A")
elif per >= 70:
    print("Grade: B")
elif per >= 60:
    print("Grade: C")
elif per >= 50:
    print("Grade: D")
else:
    print("Fail")
