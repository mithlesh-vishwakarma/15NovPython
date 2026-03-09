# # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 

# length = 20

# a = 0 # 1 1 2 3
# b = 1 # 1 2 3 5

# print(a,b,end=" ")
# # 0 1 1 2 3 5
# for i in range(length):
#     c = a+b
#     print(c,end=" ")
#     a = b
#     b = c



number = 1
sum = 1

for i in range(2,6):
    number = number *2 
    sum = sum + number

print(sum)