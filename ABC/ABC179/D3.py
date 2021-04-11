MOD = 998244353
n, k = map(int, input().split())
s = []
for _ in range(k):
    l, r = map(int, input().split())
    s.append((l, r + 1))
dp = [0] * (2 * n + 1)
dp[0] = 1
dp[1] = -1
for i in range(n):
    for l, r in s:
        dp[i + l] += dp[i]
        dp[i + r] -= dp[i]
    dp[i + 1] += dp[i]
    dp[i + 1] %= MOD
print(dp[n - 1])
