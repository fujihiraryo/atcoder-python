def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = [start]
    for x in queue:
        for y in graph[x]:
            if dist[y] != -1:
                continue
            queue.append(y)
            dist[y] = dist[x] + 1
    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
k = int(input())
mat = [[0] * k for _ in range(k)]
(*c,) = map(lambda x: int(x) - 1, input().split())
for i in range(k):
    dist = bfs(graph, c[i])
    for j in range(k):
        mat[i][j] = dist[c[j]]
        if dist[c[j]] == -1:
            print(-1)
            exit()
dp = [[1 << 30] * k for _ in range(1 << k)]
dp[0][0] = 0
for s in range(1 << k):
    for i in range(k):
        dp[1 << i][i] = 0
        if (1 << i) & s:
            for j in range(k):
                if (1 << j) & s:
                    dp[s][i] = min(dp[s][i], dp[s - (1 << i)][j] + mat[j][i])
print(min(dp[(1 << k) - 1]) + 1)
