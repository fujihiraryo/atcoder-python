n, k = map(int, input().split())
cnt = [0] * (n + 1)
for i in range(2, n + 1):
    if cnt[i]:
        continue
    for j in range(i, n + 1, i):
        cnt[j] += 1
ans = 0
for i in range(2, n + 1):
    if cnt[i] >= k:
        ans += 1
print(ans)
