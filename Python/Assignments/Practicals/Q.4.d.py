# Practical Example 8: Write a Python program to check if a person is eligible to donate blood
# using a nested if.

# take input
age = int(input("Enter age: "))
weight = float(input("Enter weight: "))

# check eligibility
if age >= 18:
    if weight >= 50:
        print("You can donate blood")
    else:
        print("You cannot donate blood (low weight)")
else:
    print("You cannot donate blood (age less than 18)")
