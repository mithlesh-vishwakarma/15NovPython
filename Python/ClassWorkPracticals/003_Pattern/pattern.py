# *****
# *****
# *****
# *****
# *****

# for j in range(5):
#     for i in range(5):
#         print("*",end="")
#     print()


# for i in range(5):
#     print(5*"*")


# *
# **
# ***
# ****
# *****

# lines = 5
# for j in range(lines):
#     for i in range(j+1):
#         print("*",end="")
#     print()


# for i in range(5):
#     print((i+1)*"*")


# *****
# ****
# ***
# **
# *

# lines = 5
# for i in range(lines):
#     for j in range(lines-i):
#         print("*",end="")
#     print()


#     *
#    **
#   ***
#  ****
# *****


# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j+1):
#         print("*",end="")
#     print()

# *****
#  ****
#   ***
#    **
#     *


# lines = 11
# for i in range(lines):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(lines-i):
#         print("*",end="")
#     print()

#    *
#   * *
#  * * *
# * * * *


# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j+1):
#         print("* ",end="")
#     print()


#       *
#      ***
#     *****
#    *******
#   *********


# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j*2+1):
#         print("*",end="")
#     print()









# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j*2+1):
#         print("*",end="")
#     print()
# for i in range(lines):
#     for k in range(i+1):
#         print(" ",end="")
#     for j in range(((lines-(i+1))*2)-1):
#         print("*",end="")
#     print()


 
#   *
#  ***
# *****
#  ***
#   *



# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j*2+1):
#         if i==0 or i==(j*2):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(lines):
#     for k in range(i+1):
#         print(" ",end="")
#     for j in range(((lines-(i+1))*2)-1):
#         if j==0 or j==(((lines-(i+1))*2)-2):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



#   *
#  * *
# *   *
#  * *
#   *