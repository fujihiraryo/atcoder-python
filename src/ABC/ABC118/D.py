n, m = map(int, input().split())
(*a,) = map(int, input().split())
match = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for x in a:
        if i - match[x] < 0 or dp[i - match[x]] == -1:
            continue
        dp[i] = max(dp[i], 10 * dp[i - match[x]] + x)
print(dp[n])
