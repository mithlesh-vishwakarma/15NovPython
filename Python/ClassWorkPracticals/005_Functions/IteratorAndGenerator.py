# l = [10, 20, 30, 40, 50, 60]
# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))


def calc(a):
    for i in range(1, a):
        yield i * i


k = calc(10)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
