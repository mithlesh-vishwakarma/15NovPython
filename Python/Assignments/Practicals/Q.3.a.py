# Q. Write a Python program to demonstrate the creation of variables and different data types.


# Integer
# age = 25

# # Float
# height = 5.9

# # String
# name = "Mithlesh"

# # Boolean
# is_developer = True

# # List (mutable sequence)
# skills = ["Python", "JavaScript", "React"]

# # Tuple (immutable sequence)
# coordinates = (10.5, 20.8)

# # Set (unique elements)
# unique_numbers = {1, 2, 3, 3, 4}

# # Dictionary (key-value pairs)
# person = {"name": name, "age": age, "height": height}

# Printing values and their types
# print("Name:", name, "| Type:", type(name))
# print("Age:", age, "| Type:", type(age))
# print("Height:", height, "| Type:", type(height))
# print("Is Developer:", is_developer, "| Type:", type(is_developer))


# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Boolean example
is_employed = True

# List (mutable sequence)
skills = ["Python", "JavaScript", "React"]

# Tuple (immutable sequence)
coordinates = (10.5, 20.8)

# Set (unique elements)
unique_numbers = {1, 2, 3, 3, 4}

# Dictionary (key-value pairs)
person = {"name": name, "age": age, "height": height}

# Display values
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Employed:", is_employed)

# Display data types
print("\n--- Data Types ---")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of employed:", type(is_employed))
print("Coordinates:", coordinates, "| Type:", type(coordinates))
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))
print("Person Info:", person, "| Type:", type(person))
print("Skills:", skills, "| Type:", type(skills))
