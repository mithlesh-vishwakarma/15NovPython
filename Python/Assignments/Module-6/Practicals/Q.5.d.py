# Practical Example 4: Print this pattern using nested for loop:
# markdown
# Copy code
# *
# **
# ***
# ****
# *****


# outer loop for rows
for i in range(1, 6):

    # inner loop for stars
    for j in range(i):
        print("*", end="")

    # move to next line
    print()
