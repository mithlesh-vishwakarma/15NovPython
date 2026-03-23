# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.

# simple calculator project


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# main program
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting program...")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", sub(num1, num2))
        elif choice == "3":
            print("Result:", mul(num1, num2))
        elif choice == "4":
            print("Result:", div(num1, num2))
    else:
        print("Invalid choice, try again")
