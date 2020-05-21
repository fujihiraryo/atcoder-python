from math import gcd
n = int(input())
C = {}
z = 0
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        z += 1
        continue
    g = gcd(x, y)
    x, y = x // g, y // g
    if y < 0:
        x, y = -x, -y
    try:
        C[(x, y)] += 1
    except KeyError:
        C[(x, y)] = 1
ans = 1
p = 10**9 + 7
for x, y in C:
    if C[(x, y)] == 0:
        continue
    a = C[(x, y)]
    if x > 0:
        x0, y0 = -y, x
    else:
        x0, y0 = y, -x
    try:
        b = C[(x0, y0)]
        C[(x0, y0)] = 0
    except KeyError:
        b = 0
    ans *= pow(2, a, p) + pow(2, b, p) - 1
    ans %= p
    C[(x, y)] = 0
print((ans + z - 1) % p)
