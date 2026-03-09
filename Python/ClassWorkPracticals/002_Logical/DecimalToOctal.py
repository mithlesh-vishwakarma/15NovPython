number = 456
sum = 0
m = 1
while number!=0:
    rem = number%8
    sum = sum+(rem*m)
    number//=8
    m*=10

print(sum)