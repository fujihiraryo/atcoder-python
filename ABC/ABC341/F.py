def knapsack(n, m, v, w):
    # n: アイテムの個数
    # m: ナップサックの容量
    # v[i]: アイテムiの価値
    # w[i]: アイテムiの重さ
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m + 1):
            if w[i] <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[n][m]


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)
(*w,) = map(int, input().split())
(*a,) = map(int, input().split())
idx = list(range(n))
idx.sort(key=lambda i: w[i])
c = [0] * n
for i in idx:
    v = [c[j] for j in g[i]]
    q = [w[j] for j in g[i]]
    c[i] = 1 + knapsack(len(g[i]), w[i] - 1, v, q)
ans = sum(a[i] * c[i] for i in range(n))
print(ans)
