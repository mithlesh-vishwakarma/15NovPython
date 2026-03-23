# Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition.

# list of fruits
list1 = ["apple", "banana", "mango"]

# take input from user
item = input("Enter fruit to search: ")

# check using loop
found = False

for fruit in list1:
    if fruit == item:
        found = True

# result
if found:
    print("Found in list")
else:
    print("Not found")
