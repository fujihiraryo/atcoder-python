import random

n = 10 ** 3
m = 10 ** 5
print(n)
print(*[random.choice(range(1, m + 1)) for _ in range(n)])
