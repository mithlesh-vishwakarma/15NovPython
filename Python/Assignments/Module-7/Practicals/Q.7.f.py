# Write a Python program to count how many times each character appears in a string.

# Creating a string
my_string = "programming"

# Printing the string
print("String:", my_string)

# Counting character frequencies
char_count = {}
for char in my_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Printing character frequencies
print("\nCharacter frequencies:")
for char, count in char_count.items():
    print(f"{char}: {count}")
