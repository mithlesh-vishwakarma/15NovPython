from functools import reduce

# sub = ["python", "php", "java", "node", "android"]

# k = map(lambda x: len(x), sub)

# print(list(k))

# k = filter(lambda x: "a" in x, sub)
# print(list(k))
# k = filter(lambda x: x.startswith("p"), sub)
# print(list(k))


l = [2, 5, 9, 8, 25, 49, 45, 81, 144, 22, 33]

# k = filter(lambda x: x**0.50 == x**2, l)
# print(list(k))

k = filter(lambda a, b: a if a > b else b, l)
print(k)
