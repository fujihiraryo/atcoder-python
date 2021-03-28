MOD = 998244353
n, m = map(int, input().split())
fct, ict = [1], [1]
for i in range(1, n + 1):
    fct.append(fct[-1] * i % MOD)
    ict.append(ict[-1] * pow(i, MOD - 2, MOD) % MOD)
dp = [0] * (m + 1)
dp[0] = 1
for i in range(2, m + 1, 2):
    for j in range(0, min(i, n) + 1, 2):
        dp[i] += fct[n] * ict[j] * ict[n - j] * dp[(i - j) // 2]
        dp[i] %= MOD
print(dp[m])
