h, w = map(int, input().split())
a = [[1 if x == "+" else -1 for x in input()] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (i + j) % 2 == 0:
            a[i][j] *= -1
dp = [[0] * w for _ in range(h)]
for i in range(h)[::-1]:
    for j in range(w)[::-1]:
        if i == h - 1 and j == w - 1:
            continue
        if i == h - 1:
            dp[i][j] = dp[i][j + 1] + a[i][j + 1]
            continue
        if j == w - 1:
            dp[i][j] = dp[i + 1][j] + a[i + 1][j]
            continue
        if (i + j) % 2 == 0:
            dp[i][j] = max(dp[i + 1][j] + a[i + 1][j], dp[i][j + 1] + a[i][j + 1])
        else:
            dp[i][j] = min(dp[i + 1][j] + a[i + 1][j], dp[i][j + 1] + a[i][j + 1])
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] == 0:
    print("Draw")
else:
    print("Aoki")
