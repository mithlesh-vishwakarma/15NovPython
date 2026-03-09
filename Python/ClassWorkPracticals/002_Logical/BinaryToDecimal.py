# number = 456
# sum = 0
# m = 1
# while number!=0:
#     rem = number%2
#     sum = sum+(rem*m)
#     number//=2
#     m*=10

# print(sum)


#10011011: 1+2+0+8+16+0+0= 155 -> binary into decimal. 
#get reminder by deviding by 10 and then multiply it with 2's power from 0,1,2,3,4, and so on...

number = 1001101101
sum=0
m=0

while number!=0:
  rem = number%10
  number=number//10
  sum += rem*pow(2,m)
  m=m+1
print(sum)