# import random

# a, b, c = map(int, input().split())


def ans(a, b, c):
    return pow(a, pow(b, c, 4) + 4, 10)


def test(a, b, c):
    return pow(a, pow(b, c), 10)


# for i in range(100):
#     a = random.randrange(1, 20)
#     b = random.randrange(1, 20)
#     c = random.randrange(1, 20)
#     assert ans(a, b, c) == test(a, b, c)
a, b, c = map(int, input().split())
print(ans(a, b, c))
