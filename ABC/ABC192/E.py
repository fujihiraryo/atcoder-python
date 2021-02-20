import heapq

INF = 1 << 60


n, m, start, goal = map(int, input().split())
start -= 1
goal -= 1
sub_graph = [[] for _ in range(n)]
for _ in range(m):
    ai, bi, ti, ki = map(int, input().split())
    sub_graph[ai - 1].append((bi - 1, ti, ki))
    sub_graph[bi - 1].append((ai - 1, ti, ki))


def graph(t, x):
    # 時刻,場所
    for y, c, k in sub_graph[x]:
        # t以上の最小のkの倍数
        tmp = k * (-(-t // k))
        yield tmp + c, y


dist = [INF] * n
dist[start] = 0
heap = [(0, start)]
heapq.heapify(heap)
while heap:
    t, x = heapq.heappop(heap)
    if dist[x] < t:
        continue
    for s, y in graph(t, x):
        if dist[y] > s:
            dist[y] = s
            heapq.heappush(heap, (s, y))
if dist[goal] == INF:
    print(-1)
else:
    print(dist[goal])
