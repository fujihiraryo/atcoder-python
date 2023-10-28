import bisect

n, m = map(int, input().split())
(*a,) = map(int, input().split())
a.sort()
ans = 0
for i in range(n):
    j = bisect.bisect_left(a, a[i] + m)
    ans = max(ans, j - i)
print(ans)
