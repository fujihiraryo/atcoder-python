h, w = map(int, input().split())
p = []
for _ in range(h):
    p.append(list(map(int, input().split())))
ans = 0
for s in range(1, 1 << h):
    cnt = [0] * h * w
    for j in range(w):
        lst = []
        for i in range(h):
            if not (1 << i) & s:
                continue
            lst.append(p[i][j] - 1)
        lst.sort()
        if lst[0] == lst[-1]:
            # 列に含まれる数字が1種類
            cnt[lst[0]] += 1
    ans = max(ans, max(cnt) * bin(s).count("1"))
print(ans)
