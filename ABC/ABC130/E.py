MOD = 10 ** 9 + 7
n, m = map(int, input().split())
(*s,) = map(int, input().split())
(*t,) = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] + 1) % MOD
        else:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]) % MOD
print((dp[n][m] + 1) % MOD)
