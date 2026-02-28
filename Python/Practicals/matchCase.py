print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
action=input("Enter a number: ")
match action:
  case "1":
    print("You have chosen to add two numbers")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1+num2)
  case "2":
    print("You have chosen to subtract two numbers")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1-num2)
  case "3":
    print("You have chosen to multiply two numbers")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print(num1*num2)
  case "4":
    print("You have chosen to divide two numbers")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    if num2!=0:
      print(num1/num2)
    else:
      print("Cannot divide by zero")
  case "5":
    print("You have chosen to modulus two numbers")
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    if num2!=0:
      print(num1%num2)
    else:
      print("Cannot modulus by zero")
  case _:
    print("Invalid input please choose correct option")