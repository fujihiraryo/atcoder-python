INF = 1 << 60
n, m = map(int, input().split())
graph = [set() for _ in range(n)]
char = [[None] * n for _ in range(n)]
for _ in range(m):
    a, b, c = input().split()
    a, b = int(a) - 1, int(b) - 1
    char[a][b] = c
    char[b][a] = c
    graph[a].add(b)
    graph[b].add(a)
dist = [[INF] * n for _ in range(n)]
dist[0][n - 1] = 0
queue = [(0, n - 1)]
for i, j in queue:
    for x in graph[i]:
        for y in graph[j]:
            if char[i][x] == char[j][y] and dist[x][y] == INF:
                queue.append((x, y))
                dist[x][y] = dist[i][j] + 1
ans = INF
for i in range(n):
    for j in range(n):
        if i == j:
            ans = min(ans, 2 * dist[i][j])
        if j in graph[i]:
            ans = min(ans, 2 * dist[i][j] + 1)
print(ans if ans < INF else -1)
