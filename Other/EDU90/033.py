from itertools import product

h, w = map(int, input().split())
if h == 1:
    print(w)
    exit()
if w == 1:
    print(h)
    exit()
light = [[0] * w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        ok = 1
        for di, dj in product((-1, 0, 1), (-1, 0, 1)):
            if 0 <= i + di < h and 0 <= j + dj < w and light[i + di][j + dj]:
                ok = 0
        if ok:
            light[i][j] = 1
            ans += 1
print(ans)
