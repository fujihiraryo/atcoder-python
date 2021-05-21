INF = 10 ** 20
n, k = map(int, input().split())
x, y = [None] * n, [None] * n
for i in range(n):
    xi, yi = map(int, input().split())
    x[i] = xi
    y[i] = yi

cost = [0] * (1 << n)
for s in range(1 << n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (1 << i) & s and (1 << j) & s:
                cost[s] = max(cost[s], (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

dp = [[INF] * (1 << n) for _ in range(k + 1)]
dp[0][0] = 0
for s in range(1, 1 << n):
    lim = min(k, bin(s).count("1"))
    for i in range(1, lim + 1):
        t = s
        while t * 2 > s:
            dp[i][s] = min(dp[i][s], max(dp[i - 1][s - t], cost[t]))
            t = (t - 1) & s
print(dp[k][(1 << n) - 1])
