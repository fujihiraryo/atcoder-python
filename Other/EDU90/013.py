import heapq

INF = 1 << 30


def dijkstra(graph, start):
    dist = [INF] * len(graph)
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    while heap:
        d, x = heapq.heappop(heap)
        if dist[x] < d:
            continue
        for y in graph[x]:
            if dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
                heapq.heappush(heap, (dist[y], y))
    return dist


n, m = map(int, input().split())
graph = [{} for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
dist0 = dijkstra(graph, 0)
dist1 = dijkstra(graph, n - 1)
for x in range(n):
    print(dist0[x] + dist1[x])
