number = 456
sum = 0
m = 1
while number!=0:
    rem = number%2
    sum = sum+(rem*m)
    number//=2
    m*=10

print(sum)