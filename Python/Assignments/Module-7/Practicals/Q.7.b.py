# Write a Python program to merge two lists into one dictionary using a loop.

# Creating two lists
keys = ["name", "age", "city"]
values = ["Mithlesh", 25, "Surat"]

# Creating a dictionary using a loop
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# Printing the dictionary
print("Dictionary created from two lists:")
print(my_dict)