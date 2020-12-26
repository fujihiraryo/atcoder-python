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


n = 5
graph = [[] for _ in range(n)]
edge = [(0, 1), (1, 2), (2, 3), (2, 4)]
for a, b in edge:
    graph[a].append(b)
    graph[b].append(a)
print(bfs(graph, 0))
print(bfs(graph, 1))
