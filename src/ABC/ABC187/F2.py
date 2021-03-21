n, m = map(int, input().split())
graph = [1 << i for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1] |= 1 << (b - 1)
    graph[b - 1] |= 1 << (a - 1)
dp = [n] * (1 << n)
dp[0] = 0
for s in range(1, 1 << n):
    # 完全部分グラフの場合
    if all((s & graph[i]) == s for i in range(n) if (1 << i) & s):
        dp[s] = 1
        continue
    # その他
    t = s
    while t:
        t = (t - 1) & s
        dp[s] = min(dp[s], dp[t] + dp[s - t])
print(dp[(1 << n) - 1])
