from collections import defaultdict

INF = 1 << 30
n, m, p = map(int, input().split())
edge_list = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge_list.append((a - 1, b - 1, -(c - p)))
# 0から各頂点へ行けるか
graph = [[] for _ in range(n)]
for a, b, _ in edge_list:
    graph[a].append(b)
from_start = [0] * n
stack = [0]
while stack:
    x = stack.pop()
    from_start[x] = 1
    for y in graph[x]:
        if from_start[y]:
            continue
        stack.append(y)
# 各頂点からn-1へ行けるか
graph = [[] for _ in range(n)]
for a, b, _ in edge_list:
    graph[b].append(a)
to_goal = [0] * n
stack = [n - 1]
while stack:
    x = stack.pop()
    to_goal[x] = 1
    for y in graph[x]:
        if to_goal[y]:
            continue
        stack.append(y)
# 0から行けてn-1へ行ける頂点だけでグラフを作りベルマンフォード
graph = [defaultdict(lambda: INF) for _ in range(n)]
for a, b, c in edge_list:
    if all([from_start[a], from_start[b], to_goal[a], to_goal[b]]):
        graph[a][b] = min(graph[a][b], c)
dist = [INF] * n
dist[0] = 0
update = 1
cnt = 0
while update:
    update = 0
    cnt += 1
    if cnt > n:
        print(-1)
        exit()
    for x in range(n):
        for y in graph[x]:
            if dist[x] < INF and dist[x] + graph[x][y] < dist[y]:
                dist[y] = dist[x] + graph[x][y]
                update = 1
print(max(0, -dist[n - 1]))
