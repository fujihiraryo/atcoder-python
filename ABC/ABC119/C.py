import itertools

INF = 10 ** 9
n, a, b, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
mincost = INF
for s in itertools.product(range(4), repeat=n):
    x, y, z = 0, 0, 0
    cx, cy, cz = 0, 0, 0
    for i in range(n):
        if s[i] == 0:
            x += lst[i]
            cx += 1
        if s[i] == 1:
            y += lst[i]
            cy += 1
        if s[i] == 2:
            z += lst[i]
            cz += 1
    if cx * cy * cz == 0:
        continue
    cnt = cx + cy + cz - 3
    cost = abs(a - x) + abs(b - y) + abs(c - z) + 10 * cnt
    mincost = min(mincost, cost)
print(mincost)
