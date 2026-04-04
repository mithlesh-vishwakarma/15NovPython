# Write a Python program to create a calculator using functions.

# Creating functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing calculations
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
