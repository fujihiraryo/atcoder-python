INF = 1 << 64
n, m = map(int, input().split())
a, c = [], []
for _ in range(m):
    ai, bi = map(int, input().split())
    a.append(ai)
    c.append(sum(1 << (ci - 1) for ci in map(int, input().split())))
dp = [[INF] * (m + 1) for _ in range(1 << n)]
for i in range(m + 1):
    dp[0][i] = 0
for s in range(1, 1 << n):
    for i in range(1, m + 1):
        dp[s][i] = min(dp[s ^ (s & c[i - 1])][i - 1] + a[i - 1], dp[s][i - 1])
ans = dp[(1 << n) - 1][m]
print(-1 if ans == INF else ans)
