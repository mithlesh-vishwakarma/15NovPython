# number = 456
# sum =""
#
# while number!=0:
#     rem = number%16
#     sum = sum+k[rem]
#     number = number//16
# print(sum)

number = "1C8"
k = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

sum = 0
m = 0

for i in number[::-1]:
    value = k.index(i)
    sum += value * pow(16, m)
    m += 1

print(sum)