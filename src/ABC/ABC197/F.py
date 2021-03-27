n, m = map(int, input().split())
graph = [[] for _ in range(n)]
char = [[None] * n for _ in range(n)]
for _ in range(m):
    a, b, c = input().split()
    a, b = int(a) - 1, int(b) - 1
    char[a][b] = c
    char[b][a] = c
    graph[a].append(b)
    graph[b].append(a)
dist = [[-1] * n for _ in range(n)]
dist[0][n - 1] = 0
queue = [(0, n - 1)]
for i, j in queue:
    for x in graph[i]:
        for y in graph[j]:
            if char[i][x] == char[j][y] and dist[x][y] == -1:
                queue.append((x, y))
                dist[x][y] = dist[i][j] + 1
print(dist[n - 1][0])
