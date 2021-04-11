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


h, w = map(int, input().split())
s = [input() for _ in range(h)]
graph = [[] for _ in range(h * w)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        x = i * w + j
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= i + di < h and 0 <= j + dj < w and s[i + di][j + dj] == ".":
                y = (i + di) * w + j + dj
                graph[x].append(y)

ans = 0
for x in range(h * w):
    dist = bfs(graph, x)
    ans = max(ans, max(dist))
print(ans)
