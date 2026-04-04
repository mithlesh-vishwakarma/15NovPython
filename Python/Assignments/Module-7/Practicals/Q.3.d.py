# Write a Python program to insert elements into an empty list using a for loop and append().

# Creating an empty list
my_list = []

# Inserting elements using a for loop and append()
print("Inserting elements into an empty list:")
for i in range(5):
    element = i * 10
    my_list.append(element)
    print(f"Appended {element}, list is now: {my_list}")

# Inserting different types of elements
print("\nInserting different types of elements:")
for item in ["Apple", 20, 3.14, True]:
    my_list.append(item)
    print(f"Appended {item}, list is now: {my_list}")