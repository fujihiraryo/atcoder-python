from math import gcd
n = int(input())
P = [tuple(map(int, input().split())) for i in range(n)]
C = {}
for x, y in P:
    if x == 0 and y == 0:
        x0, y0 = 0, 0
    elif x != 0 and y == 0:
        x0, y0 = 1, 0
    elif x == 0 and y != 0:
        x0, y0 = 0, 1
    else:
        g = gcd(x, y)
        x0, y0 = x // g, y // g
    if y0 < 0:
        x0, y0 = -x0, -y0
    try:
        C[(x0, y0)] += 1
    except KeyError:
        C[(x0, y0)] = 1
D = []
for x, y in C.keys():
    if x <= 0:
        try:
            C[(y, -x)]
        except KeyError:
            D.append((y, -x))
for x, y in D:
    C[(x, y)] = 0
ans = 1
p = 10**9 + 7
for x, y in C.keys():
    if x > 0:
        a = C[(x, y)]
        try:
            b = C[(-y, x)]
        except KeyError:
            b = 0
        ans *= pow(2, a, p) + pow(2, b, p) - 1
        ans %= p
try:
    ans += C[(0, 0)] - 1
except KeyError:
    ans -= 1
print(ans % p)
