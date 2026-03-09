number = 153
temp = number
count = 0
sum = 0

# Count digits
while number != 0:
    count = count + 1
    number = number // 10

number = temp  # restore number

# Calculate Armstrong sum
while number != 0:
    rem = number % 10
    sum += pow(rem, count)
    number = number // 10

print(count)

if temp == sum:
    print(f"{temp} is Armstrong number")
else:
    print(f"{temp} is not Armstrong number")