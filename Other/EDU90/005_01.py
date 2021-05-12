MOD = 10 ** 9 + 7
n, b, k = map(int, input().split())
if n > 10000:
    exit()
*lst, = map(int, input().split())
dp = [[0] * b for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(b):
        for c in lst:
            dp[i + 1][(10 * j + c) % b] += dp[i][j]
            dp[i + 1][j] %= MOD
print(dp[n][0])
