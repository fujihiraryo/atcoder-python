import random

h, w, m = 5, 5, 5
print(h, w, m)
for _ in range(m):
    x, y = random.choice(range(h)), random.choice(range(1, w))
    print(x + 1, y + 1)
