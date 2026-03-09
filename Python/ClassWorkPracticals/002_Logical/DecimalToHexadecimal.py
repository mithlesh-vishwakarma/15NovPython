# number = 456
# sum =""
# k = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# while number!=0:
#     rem = number%16
#     sum = sum+k[rem]
#     number = number//16
# print(sum)


number = 456
sum =""
k = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}
while number!=0:
    rem = number%16
    if rem>=10:
        sum = sum+k[rem]
    else :
        sum  = sum+str(rem)
    number//=16

print(sum)