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


r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
graph = [[] for _ in range(r * c)]
for i in range(r):
    for j in range(c):
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if i + di < 0 or i + di >= r or j + dj < 0 or j + dj >= c:
                continue
            graph[i * c + j].append((i + di) * c + j + dj)
dist = bfs(graph, 0)
ans = 0
for i in range(r):
    for j in range(c):
        if dist[i * c + j] <= d and dist[i * c + j] % 2 == d % 2:
            ans = max(ans, a[i][j])
print(ans)
