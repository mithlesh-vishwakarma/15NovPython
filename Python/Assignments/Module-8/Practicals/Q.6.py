# Q.6 Write a Python program to check the current position of the file cursor using tell().

try:
    with open("sample.txt", "r") as file:
        print("Initial position:", file.tell())
        file.read(5)
        print("Position after reading 5 characters:", file.tell())
except FileNotFoundError:
    print("File not found.")
