MOD = 10 ** 9 + 7
n = int(input())
s = input()
t = "atcoder"
m = len(t)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    dp[i][0] = 1
    for j in range(m):
        dp[i + 1][j + 1] += dp[i][j + 1]
        if s[i] == t[j]:
            dp[i + 1][j + 1] += dp[i][j]
        dp[i + 1][j + 1] %= MOD
print(dp[n][m])
