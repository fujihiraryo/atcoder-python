from bisect import bisect

n, k = map(int, input().split())
m = 30
*a, = map(int, input().split())
a.sort()
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m + 1):
        dp[i + 1][j] = dp[i][j] + 1
    x = bisect(a, a[i] // 2)
    for j in range(m):
        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[x][j])
ans = min((j, dp[n][j]) for j in range(m + 1) if dp[n][j] <= k)
print(*ans)
