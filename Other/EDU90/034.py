n, k = map(int, input().split())
*a, = map(int, input().split())
j = 0
cnt = {}
ans = 0
for i in range(n):
    while j < n and (len(cnt) < k or a[j] in cnt):
        if a[j] in cnt:
            cnt[a[j]] += 1
        else:
            cnt[a[j]] = 1
        j += 1
    ans = max(ans, j - i)
    cnt[a[i]] -= 1
    if cnt[a[i]] == 0:
        cnt.pop(a[i])
print(ans)
