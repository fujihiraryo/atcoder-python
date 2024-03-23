n, k = map(int, input().split())
(*a,) = map(int, input().split())
s = set()
for i in range(n):
    if a[i] <= k:
        s.add(a[i])
ans = k * (k + 1) // 2 - sum(s)
print(ans)
