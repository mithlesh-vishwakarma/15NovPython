# *
# **
# ***
# ****
# *****

# lines = 5
# stars = 1
# for i in range(lines):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1


# *****
# ****
# ***
# **
# *


# lines = 5
# stars = lines
# for i in range(lines):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1


#     *
#    **
#   ***
#  ****
# *****


# lines = 5
# stars = 1
# space=lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1
#     space-=1


# *****
#  ****
#   ***
#    **
#     *


# lines = 5
# stars = lines
# space=0
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1
#     space+=1


#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# lines = 5
# stars = 1
# space=lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("* ",end="")
#     print()
#     stars+=1
#     space-=1


#     *
#    ***
#   *****
#  *******
# *********



# lines = 5
# stars = 1
# space=lines-1
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=2
#     space-=1


# lines = 9
# stars = 1
# space=lines-1
# mid = (lines//2)
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else:
#         stars-=2
#         space+=1




# lines = 19
# stars = 1
# space=lines-1
# mid = (lines//2)
# for i in range(lines):
#     for k in range(space):
#         print(" ",end="")
#     for j in range(stars):
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=2
#         space-=1
#     else:
#         stars-=2
#         space+=1