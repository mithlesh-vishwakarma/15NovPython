# Q.4 Write a Python program to create a file and print the string into the file.

with open("sample2.txt", "w") as file:
    print("This string is printed directly into the file.", file=file)
print("String printed to file successfully.")
