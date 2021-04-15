n = int(input())
for k in range(1, n + 1):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        dp[i + 1] = 1 + dp[i + 1 - k] + dp[i]
    print(dp[1:])
