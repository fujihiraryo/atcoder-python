S = list(input())
S.reverse()
N = len(S)
mod = 10**9+7
dp = [[0 for r in range(13)] for n in range(N+1)]
dp[0][0] = 1
lookup = [[0 for d in range(10)] for n in range(N)]
for n in range(N):
    for d in range(10):
        lookup[n][d] = d*pow(10, n, 13) % 13
for n in range(1, N+1):
    if S[n-1] == '?':
        for d in range(10):
            for r in range(13):
                dp[n][(r+lookup[n-1][d]) % 13] += dp[n-1][r] % mod
    else:
        for r in range(13):
            dp[n][(r+lookup[n-1][int(S[n-1])]) % 13] += dp[n-1][r] % mod
print(dp[-1][5] % mod)
