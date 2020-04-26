def fibb(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

x=fibb(72)
print(list(x))