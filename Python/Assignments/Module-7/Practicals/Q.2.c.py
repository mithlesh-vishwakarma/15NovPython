# Write a Python program to update a list using insert() and append().

# Creating a list
my_list = [10, 20, 30, 40]
print("Original list:", my_list)

# Updating elements using index assignment
my_list[1] = 25  # Update element at index 1
print("After updating index 1:", my_list)

# Updating multiple elements using slicing
my_list[0:2] = [5, 15]  # Update first two elements
print("After updating slice 0:2:", my_list)

# Adding elements using append()
my_list.append(50)
print("After append(50):", my_list)

# Adding multiple elements using append() with iterable
my_list.append([60, 70])
print("After append([60, 70]):", my_list)

# Adding elements using insert()
my_list.insert(2, 22)  # Insert at index 2
print("After insert(2, 22):", my_list)

# Adding multiple elements using insert() with iterable
my_list.insert(0, [1, 2])  # Insert at beginning
print("After insert(0, [1, 2]):", my_list)
