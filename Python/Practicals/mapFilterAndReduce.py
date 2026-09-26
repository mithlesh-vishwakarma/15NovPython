from functools import reduce
a=[1,3,5,98,7,8,4,2]

# odd number:

result=filter(lambda x:x%2!=0,a)
print(f"odd number: {result}")

# square:

result= map(lambda x:x**2,a)
print(f"Square: {result}")


# total:

result= reduce(lambda x,y: x+y,a)
print(f"Total: {result}")

