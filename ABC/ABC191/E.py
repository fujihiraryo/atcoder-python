import heapq

INF = 1 << 30


def dijkstra(graph, start):
    dist = [INF] * len(graph)
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    while heap:
        _, x = heapq.heappop(heap)
        for y in graph[x]:
            if dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
                heapq.heappush(heap, (dist[y], y))
    return dist


n, m = map(int, input().split())
graph = [{} for _ in range(2 * n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b += n - 1
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c
for x in range(n, 2 * n):
    graph[x][x - n] = 0
for x in range(n):
    ans = dijkstra(graph, x)[x + n]
    print(ans if ans < INF else -1)
