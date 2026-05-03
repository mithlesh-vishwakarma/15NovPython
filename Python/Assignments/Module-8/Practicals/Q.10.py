# Q.10 Write a Python program to print custom exceptions.

class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed."):
        self.message = message
        super().__init__(self.message)

try:
    # num = int(input("Enter a positive number: "))
    num = -5 # Hardcoded for demonstration
    if num < 0:
        raise NegativeNumberError()
    print(f"You entered: {num}")
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}")
except ValueError:
    print("Invalid input.")
