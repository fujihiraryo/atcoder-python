def breadth_first_search(graph, start, goal):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = [start]
    for x in queue:
        if x == goal:
            break
        for y in graph[x]:
            if dist[y] == -1:
                queue.append(y)
                dist[y] = dist[x] + 1
    return dist[goal]


n, m = map(int, input().split())
graph = [[] for _ in range(3 * n)]
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    graph[x].append(y + n)
    graph[x + n].append(y + 2 * n)
    graph[x + 2 * n].append(y)
start, goal = map(lambda x: int(x) - 1, input().split())
ans = breadth_first_search(graph, start, goal)
if ans == -1:
    print(-1)
else:
    print(ans // 3)
