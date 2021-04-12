s = input()
t = "atcoder"
n, m = len(s), len(t)
# dp[i][j] = s[0:i]に含まれるt[0:j]の個数
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    dp[i][0] = 1
    for j in range(m):
        dp[i + 1][j + 1] += dp[i][j + 1]
        if s[i] == t[j]:
            dp[i + 1][j + 1] += dp[i][j]
print(dp[n][m])
