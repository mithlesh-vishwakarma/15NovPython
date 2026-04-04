# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']


# list of fruits
list1 = ["apple", "banana", "mango"]

# loop through list
for fruit in list1:
    if fruit == "banana":
        continue
    print(fruit)
