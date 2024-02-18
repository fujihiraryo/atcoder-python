# PyPy: MLE
# CPython AC
n, m, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
dp = [0] * n
# dp[y]>>x = xからyに到達可能
for x in range(n):
    dp[x] |= 1 << x
for x in range(n):
    for y in g[x]:
        dp[y] |= dp[x]
for _ in range(q):
    x, y = map(int, input().split())
    print("Yes" if (dp[y - 1] >> x - 1) & 1 else "No")
