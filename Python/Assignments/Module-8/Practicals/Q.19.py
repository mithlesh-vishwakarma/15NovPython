# Q.19 Write a Python program to show method overloading. 
# Python does not support traditional method overloading, but we can use default arguments or variable-length arguments.

class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

math_op = MathOperations()
print("Add 1 num:", math_op.add(5))
print("Add 2 nums:", math_op.add(5, 10))
print("Add 3 nums:", math_op.add(5, 10, 15))
