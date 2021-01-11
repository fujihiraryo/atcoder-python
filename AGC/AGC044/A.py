from collections import defaultdict
import heapq


def adj(x):
    global a, b, c, d
    return (
        (0, x * d),
        (-(-x // 2), (2 - x % 2) * d + a),
        (x // 2, (x % 2) * d + a),
        (-(-x // 3), (3 - x % 3) * d + b),
        (x // 3, (x % 3) * d + b),
        (-(-x // 5), (5 - x % 5) * d + c),
        (x // 5, (x % 5) * d + c),
    )


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


for _ in range(int(input())):
    n, a, b, c, d = map(int, input().split())
    print(dijkstra(n, 0))
