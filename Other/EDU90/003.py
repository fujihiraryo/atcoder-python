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


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
dist0 = bfs(graph, 0)
x = max(range(n), key=lambda x: dist0[x])
distx = bfs(graph, x)
y = max(range(n), key=lambda x: distx[x])
print(distx[y] + 1)
