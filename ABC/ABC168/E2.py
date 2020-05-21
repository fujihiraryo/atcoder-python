from collections import defaultdict
from math import gcd
C = defaultdict(lambda: 0)
for i in range(int(input())):
    x, y = map(int, input().split())
    g = max(gcd(x, y), 1)
    x, y = x // g, y // g
    if y < 0 or (x == -1 and y == 0):
        x, y = -x, -y
    C[(x, y)] += 1
S = set()
for x, y in C:
    if x > 0 and y >= 0:
        S.add((x, y))
    if x <= 0 and y > 0:
        S.add((y, -x))
ans = 1
p = 10**9 + 7
for x, y in S:
    ans *= pow(2, C[(x, y)], p) + pow(2, C[(-y, x)], p) - 1
    ans %= p
print((ans + C[(0, 0)] - 1) % p)
