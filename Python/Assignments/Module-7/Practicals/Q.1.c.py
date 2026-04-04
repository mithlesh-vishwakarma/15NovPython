# Write a Python program to create a list of multiple data type elements

# Creating a list with different data types
multi_list = [25, "Mithlesh", 7.89, False, [1, 2, 3], ("a", "b"), {"key": "value"}]

# Display the list
print("List with multiple data types:")
print(multi_list)

# Display type of each element
print("\nTypes of elements in the list:")
for element in multi_list:
    print(element, "->", type(element))