anon = lambda x: x * 2


def double(x):
    return x * 2

print(anon)
print(lambda x: x * 2)
print(double)

print(anon(7))
print(double(7))
