r, c, k = map(int, input().split())
value = [[0] * c for _ in range(r)]
for _ in range(k):
    x, y, v = map(int, input().split())
    value[x - 1][y - 1] = v
dp = [[[0] * 4 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        for k in range(1, 4):
            if i + j == 0:
                dp[i][j][k] = value[i][j]
            if i > 0:
                dp[i][j][k] = dp[i - 1][j][3] + value[i][j]
            if j > 0:
                dp[i][j][k] = max(
                    dp[i][j][k], dp[i][j - 1][k - 1] + value[i][j], dp[i][j - 1][k]
                )
print(dp[r - 1][c - 1][3])
