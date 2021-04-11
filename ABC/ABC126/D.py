n = int(input())
graph = [{} for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u][v] = w % 2
    graph[v][u] = w % 2
color = [None] * n
quene = [0]
color[0] = 0
for x in quene:
    for y in graph[x]:
        if color[y] is not None:
            continue
        quene.append(y)
        color[y] = (color[x] + graph[x][y]) % 2
for c in color:
    print(c)
