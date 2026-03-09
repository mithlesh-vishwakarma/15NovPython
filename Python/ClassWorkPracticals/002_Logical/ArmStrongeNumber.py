# number=153
# temp=number
# sum=0
# while number!=0:
#   rem=number%10
#   sum+=pow(rem,3)
#   number=number//10
# if temp==sum:
#   print(f"{temp} is armstronge number")
# else:
#   print(f"{temp} is not armstronge number")

count=0
for i in range(100,1000):
  number=i

  temp=number
  sum=0
 
  while number !=0:
    rem=number%10
    sum+=pow(rem,3)
    number=number//10
if temp==sum:
    count+=1
    print(f"{count} is armstronge number")

    #binary
    #octal
    #decimal
    #hexadecimal

    #factorial using while loop?