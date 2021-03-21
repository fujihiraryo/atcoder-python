def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = [start]
    for x in queue:
        for y in graph[x]:
            if dist[y] == -1:
                queue.append(y)
                dist[y] = dist[x] + 1
    return dist


n, u, v = map(int, input().split())
u, v = u - 1, v - 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
from_u = bfs(graph, u)
from_v = bfs(graph, v)
print(max(from_v[i] for i in range(n) if from_u[i] < from_v[i]) - 1)
