MOD = 998244353
n, s = map(int, input().split())
*a, = map(int, input().split())
dp = [[0] * (s + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(s + 1):
        dp[i + 1][j] += dp[i][j]
        if j >= a[i]:
            dp[i + 1][j] += dp[i][j - a[i]]
        if j == a[i] or j == 0:
            dp[i + 1][j] += 1
ans = 0
for i in range(n):
    ans += dp[i + 1][s]
    ans %= MOD
print(ans)
