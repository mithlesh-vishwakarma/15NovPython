# Write a Python program to add elements to a list using insert() and append().

# Creating an empty list
my_list = []

# Adding elements using append()
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")
print("After append():", my_list)

# Adding elements using insert()
my_list.insert(1, "Orange")  # Insert at index 1
my_list.insert(0, "Mango")   # Insert at the beginning
print("After insert():", my_list)
