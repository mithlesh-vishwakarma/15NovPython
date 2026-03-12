# lines = 5
# num=0
# for j in range(lines):
#     for i in range(j+1):
#         num=num+1
#         print(num,end="")
#     num=0
#     print()


# 1
# 12
# 123
# 1234
# 12345



# lines = 5
# num=0
# for j in range(lines):
#     for i in range(j+1):
#         num+=1
#         print(num,end="")
#     print()


# 1
# 23
# 456
# 78910

# lines = 5
# num=5
# for j in range(lines,0,-1):
#     for i in range(j,lines+1):
#         # num-=1
#         print(j,end="")
#     # num=6
#     print()


# 5
# 44
# 333
# 2222
# 11111

# lines = 5
# num=5
# for i in range(lines,0,-1):
#     for j in range(i,lines+1):
#         num-=1
#         print(j,end="")
#     num=6
#     print()


# 5
# 45
# 345
# 2345
# 12345



lines=5
num=0
for i in range (lines):
    for j in range (i):
      print((i+j)%2,end="")
    num+=1
    print()
  

# 0
# 10
# 010
# 1010
# 010101