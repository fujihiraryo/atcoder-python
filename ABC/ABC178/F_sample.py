import random

n = 10
a = sorted([random.choice(range(1, n + 1)) for _ in range(n)])
b = sorted([random.choice(range(1, n + 1)) for _ in range(n)])
print(n)
print(*a)
print(*b)
