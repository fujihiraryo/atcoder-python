import random

MOD = 998244353
n, q = 5 * 10 ** 5, 5 * 10 ** 5
print(n, q)
a = [random.randint(0, MOD) for _ in range(n)]
print(*a)
for _ in range(q):
    t = random.randint(0, 2)
    if t == 0:
        i = random.randint(0, n - 1)
        j = random.randint(i + 1, n)
        b = random.randint(1, MOD)
        c = random.randint(0, MOD)
        print(0, i, j, b, c)
    else:
        i = random.randint(0, n - 1)
        j = random.randint(i + 1, n)
        print(1, i, j)
