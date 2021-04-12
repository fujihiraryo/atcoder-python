from functools import lru_cache

MOD = 10 ** 9 + 7

n, b, k = map(int, input().split())
(*c,) = map(int, input().split())
cnt = [0] * b
for x in c:
    cnt[x % b] += 1
m = 64
tmp = 10
pow10 = []
for _ in range(m):
    pow10.append(tmp)
    tmp *= tmp
    tmp %= b
dp = [[0] * b for _ in range(m)]
for j in range(b):
    dp[0][j] = cnt[j]
for i in range(m - 1):
    for j in range(b):
        for k in range(b):
            dp[i + 1][(pow10[i] * j + k) % b] += dp[i][j] * dp[i][k]
            dp[i + 1][(pow10[i] * j + k) % b] %= MOD


@lru_cache(maxsize=None)
def rec(n, r):
    i = n.bit_length() - 1
    if n == 1 << i:
        return dp[i][r]
    res = 0
    for j in range(b):
        res += rec(n - (1 << i), j) * dp[i][(r - pow10[i] * j) % b]
        res %= MOD
    return res


print(rec(n, 0))
