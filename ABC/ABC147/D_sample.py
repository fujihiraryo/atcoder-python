import random

n = 3 * 10 ** 5
a = [random.randrange(1 << 60) for _ in range(n)]
print(n)
print(*a)
