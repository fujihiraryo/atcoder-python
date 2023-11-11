from itertools import combinations

n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))


def dfs(x, graph, visited):
    stack = [x]
    while stack:
        x = stack.pop()
        visited[x] = 1
        for y in graph[x]:
            if visited[y]:
                continue
            stack.append(y)


def connected(graph):
    n = len(graph)
    for i in range(n):
        visited = [0] * n
        dfs(i, graph, visited)
        if not all(visited):
            return False
    return True


ans = 10**30
for lst in combinations(edges, n - 1):
    graph = [[] for _ in range(n)]
    score = 0
    for x, y, w in lst:
        graph[x].append(y)
        graph[y].append(x)
        score += w
    if connected(graph):
        ans = min(ans, score % k)
print(ans)
