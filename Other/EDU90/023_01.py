h, w = map(int, input().split())
if h >= 5 or w >= 5:
    exit()
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
    king = []
    for k in range(cnt):
        if (1 << k) & bit:
            i, j = lst[k]
            king.append((i, j))
    ok = 1
    for k, (i0, j0) in enumerate(king):
        for i1, j1 in king[k + 1 :]:
            if abs(i0 - i1) <= 1 and abs(j0 - j1) <= 1:
                ok = 0
    if ok:
        ans += 1
print(ans)
