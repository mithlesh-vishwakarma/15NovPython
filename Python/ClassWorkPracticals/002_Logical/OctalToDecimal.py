# ==================== Chintan Sir ==========================================
# number = 154
# p = 0
# sum = 0
# while number!=0:
#     rem = number%10
#     sum+=rem*pow(8,p)
#     number//=10
#     p+=1

# print(sum)
# ===========================================================================

number = 710
sum = 0
m = 0
while number!=0:
    rem = number%10
    number=number//10
    sum +=rem*pow(8,m)
    m=m+1

print(sum)