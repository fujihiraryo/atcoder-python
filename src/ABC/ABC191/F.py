from collections import defaultdict
from math import gcd

n = int(input())
(*a,) = map(int, input().split())
g = defaultdict(int)
for i in range(n):
    d = 0
    while d * d <= a[i]:
        d += 1
        if a[i] % d:
            continue
        g[d] = gcd(g[d], a[i])
        g[a[i] // d] = gcd(g[a[i] // d], a[i])
print(len([d for d in g if g[d] == d and d <= min(a)]))
