n, x = map(int, input().split())
(*a,) = map(int, input().split())
INF = 10 ** 20


def ans(m):
    dp = [[-INF] * m for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(1, m + 1)[::-1]:
            for k in range(m):
                dp[j][k] = max(dp[j - 1][(k - a[i]) % m] + a[i], dp[j][k])
    return dp[m][x % m]


print(min((x - ans(m)) // m for m in range(1, n + 1)))
