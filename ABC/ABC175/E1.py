r, c, k = map(int, input().split())
value = [[0] * c for _ in range(r)]
for _ in range(k):
    x, y, v = map(int, input().split())
    value[x - 1][y - 1] = v
dp = [[[0] * c for _ in range(r)] for _ in range(4)]
for i in range(r):
    for j in range(c):
        for k in range(1, 4):
            if i + j == 0:
                dp[k][i][j] = value[i][j]
            if i > 0:
                dp[k][i][j] = dp[3][i - 1][j] + value[i][j]
            if j > 0:
                dp[k][i][j] = max(
                    dp[k][i][j], dp[k - 1][i][j - 1] + value[i][j], dp[k][i][j - 1]
                )
print(dp[3][r - 1][c - 1])
