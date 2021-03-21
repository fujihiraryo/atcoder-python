from collections import defaultdict
import heapq


def adj(x):
    global goal
    return ((goal, abs(x - goal)), (-(-x // 2), x % 2 + 1), (x // 2, x % 2 + 1))


def dijkstra(start, goal):
    INF = 10 ** 20
    dist = defaultdict(lambda: INF)
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    while heap:
        _, x = heapq.heappop(heap)
        for y, w in adj(x):
            if dist[y] > dist[x] + w:
                dist[y] = dist[x] + w
                heapq.heappush(heap, (dist[y], y))
    return dist[goal]


goal, start = map(int, input().split())
print(dijkstra(start, goal))
