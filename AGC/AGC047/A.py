from fractions import Fraction
from collections import defaultdict

n = int(input())
a = [Fraction(input()) for _ in range(n)]


def cnt(x, p):
    y = x
    c = 0
    while y % p == 0:
        y //= p
        c += 1
    return c


b = []
for i in range(n):
    x, y = a[i].numerator, a[i].denominator
    b.append((cnt(x, 2) - cnt(y, 2), cnt(x, 5) - cnt(y, 5)))
dic = defaultdict(int)
tmp = 0
for x, y in b:
    dic[(x, y)] += 1
    if x >= 0 and y >= 0:
        tmp += 1
ans = 0
for x0, y0 in dic:
    for x1, y1 in dic:
        if x0 + x1 >= 0 and y0 + y1 >= 0:
            ans += dic[(x0, y0)] * dic[(x1, y1)]
print((ans - tmp) // 2)
