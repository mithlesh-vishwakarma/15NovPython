# Q.9 Write a Python program to handle file exceptions and use the finally block for closing the file.

file = None
try:
    file = open("sample.txt", "r")
    data = file.read()
    print("File read successfully.")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()
        print("File closed in finally block.")
