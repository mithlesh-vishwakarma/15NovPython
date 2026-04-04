# Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

# Creating a dictionary
my_dict = {
    "name": "Mithlesh",
    "age": 25,
    "city": "Surat",
    "occupation": "Student",
    "salary": 50000,
    "is_student": True
}

# Printing the dictionary
print("Dictionary with 6 key-value pairs:")
print(my_dict)

# Separating keys and values
keys = my_dict.keys()
values = my_dict.values()

# Printing keys and values
print("\nKeys:", keys)
print("Values:", values)
