n, m = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(m)]
ans = 0
for i in range(m - 1):
    li, ri = lst[i]
    for j in range(i + 1, m):
        lj, rj = lst[j]
        if li < lj < ri < rj or lj < li < rj < ri:
            ans += 1
print(ans)
