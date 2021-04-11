MOD = 998244353
two_third = 2 * pow(3, MOD - 2, MOD) % MOD
h, w, k = map(int, input().split())
right = [[0] * w for _ in range(h)]
down = [[0] * w for _ in range(h)]
for _ in range(k):
    i, j, c = input().split()
    i, j = int(i) - 1, int(j) - 1
    if c == "R" or c == "X":
        right[i][j] = 1
    if c == "D" or c == "X":
        down[i][j] = 1
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = pow(3, h * w - k, MOD)
for i in range(h):
    for j in range(w):
        dp[i][j] %= MOD
        if not right[i][j] and not down[i][j]:
            dp[i + 1][j] += dp[i][j] * two_third
            dp[i][j + 1] += dp[i][j] * two_third
        if right[i][j]:
            dp[i][j + 1] += dp[i][j]
        if down[i][j]:
            dp[i + 1][j] += dp[i][j]
print(dp[h - 1][w - 1])
