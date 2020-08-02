import random
n = 15
print(n)
for i in range(n):
    x = random.choice(range(-10000, 10000))
    y = random.choice(range(-10000, 10000))
    p = random.choice(range(1, 1000000))
    print(x, y, p)
