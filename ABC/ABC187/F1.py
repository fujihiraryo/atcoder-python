n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
dp = [n] * (1 << n)
dp[0] = 0
bit_count = [bin(s).count("1") for s in range(1 << n)]
for s in range(1, 1 << n):
    # 1点の場合
    if bit_count[s] == 1:
        dp[s] = 1
        continue
    # 完全部分グラフの場合
    comp = True
    for i in range(n - 1):
        if not (1 << i) & s:
            continue
        for j in range(i + 1, n):
            if not (1 << j) & s:
                continue
            if not graph[i][j]:
                comp = False
                break
    if comp:
        dp[s] = 1
        continue
    # その他
    t = s
    while t:
        t = (t - 1) & s
        dp[s] = min(dp[s], dp[t] + dp[s - t])
print(dp[(1 << n) - 1])
