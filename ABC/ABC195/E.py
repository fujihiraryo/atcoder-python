n = int(input())
s = [int(i) for i in input()[::-1]]
x = input()[::-1]
dp = [[0] * 7 for _ in range(n + 1)]
for j in range(1, 7):
    dp[0][j] = 1
for i in range(1, n + 1):
    k = s[i - 1] * pow(10, i - 1, 7) % 7
    for j in range(7):
        if x[i - 1] == "A":
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][(j + k) % 7])
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][(j + k) % 7])
print("Aoki" if dp[n][0] else "Takahashi")
