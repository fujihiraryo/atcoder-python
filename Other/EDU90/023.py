h, w = map(int, input().split())
c = [input() for _ in range(h)]
cnt = 0
lst = []
for i in range(h):
    for j in range(w):
        if c[i][j] == ".":
            cnt += 1
            lst.append((i, j))
ans = 0
for bit in range(1 << cnt):
    king = [[0] * w for _ in range(h)]
    for k in range(cnt):
        if (1 << k) & bit:
            i, j = lst[k]
            king[i][j] = 1
    ok = 1
    for i in range(h):
        for j in range(w):
            if king[i][j] == 0:
                continue
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    if 0 <= i + di < h and 0 <= j + dj < w and king[i + di][j + dj]:
                        ok = 0
    if ok:
        ans += 1
print(ans)
