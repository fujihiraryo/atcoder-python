n = int(input())
s = [int(i) for i in input()]
x = input()
dp = [["A"] * 7 for _ in range(n + 1)]
dp[n][0] = "T"
for i in range(n)[::-1]:
    for j in range(7):
        if x[i] == dp[i + 1][10 * j % 7]:
            dp[i][j] = dp[i + 1][10 * j % 7]
        else:
            dp[i][j] = dp[i + 1][(10 * j + s[i]) % 7]
print("Aoki" if dp[0][0] == "A" else "Takahashi")
