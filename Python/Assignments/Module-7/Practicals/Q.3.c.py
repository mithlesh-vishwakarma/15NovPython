# Write a Python program to iterate through a list and print each element.

# Creating a list
my_list = [10, 20, 30, 40, 50]
print("List elements:", my_list)

# Iterating through the list using for loop
print("\nIterating through the list:")
for element in my_list:
    print(element)

# Iterating with index
print("\nIterating with index:")
for index, element in enumerate(my_list):
    print(f"Index {index}: {element}")

# Iterating in reverse
print("\nIterating in reverse:")
for element in reversed(my_list):
    print(element)