INF = 1 << 64


def max_flow(graph, s, t):
    n = len(graph)
    res = 0
    while True:
        # bfs
        dist = [INF] * n
        dist[s] = 0
        queue = [s]
        for x in queue:
            for y in graph[x]:
                if graph[x][y] == 0 or dist[y] < INF:
                    continue
                dist[y] = dist[x] + 1
                queue.append(y)
        if dist[t] == INF:
            break
        while True:
            # dfs
            stack = [(s, INF)]
            prev = [None] * n
            while stack:
                x, f = stack.pop()
                if x == t:
                    break
                for y in graph[x]:
                    if graph[x][y] == 0 or dist[x] >= dist[y]:
                        continue
                    stack.append((y, min(f, graph[x][y])))
                    prev[y] = x
            else:
                break
            # 経路復元 & 残余グラフ更新
            y = t
            while prev[y] is not None:
                x = prev[y]
                graph[x][y] -= f
                graph[y][x] += f
                y = x
            res += f
    return res


INF = 10 ** 10
n, w = map(int, input().split())
*a, = map(int, input().split())
graph = [{} for _ in range(n + 2)]
for i in range(n):
    graph[n][i] = a[i]
    graph[i][n] = 0
    graph[i][n + 1] = w
    graph[n + 1][i] = 0
for i in range(n):
    _, *lst, = map(int, input().split())
    for j in lst:
        graph[j - 1][i] = INF
        graph[i][j - 1] = 0
ans = sum(a) - max_flow(graph, n, n + 1)
print(ans)
