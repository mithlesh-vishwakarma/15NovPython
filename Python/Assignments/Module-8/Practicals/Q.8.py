# Q.8 Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    # Division by zero
    x = 10 / 0
    
    # File not found
    with open("non_existent_file.txt", "r") as file:
        file.read()

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except FileNotFoundError:
    print("Error: The specified file was not found.")
