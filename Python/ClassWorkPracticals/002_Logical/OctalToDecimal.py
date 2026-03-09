number = 710
sum = 0
m = 0
while number!=0:
    rem = number%10
    number=number//10
    sum +=rem*pow(8,m)
    m=m+1

print(sum)