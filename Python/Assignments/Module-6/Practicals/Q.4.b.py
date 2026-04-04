# Practical Example 6: Write a Python program to check if a number is prime using if_else

# take input from user
num = int(input("Enter a number: "))

# assume number is prime
is_prime = True

# check conditions
if num <= 1:
    is_prime = False
else:
    # check divisibility
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# output result
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
