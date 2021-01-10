import random

n = 4
m = 4
print(n)
for _ in range(n):
    x = random.choice(range(m))
    y = random.choice(range(m))
    print(x + 1, y + 1)
