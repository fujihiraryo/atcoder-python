def topological_sort(dag):
    n = len(dag)
    src = [set() for _ in range(n)]
    tgt = [set() for _ in range(n)]
    stack = set(range(n))
    for x in range(n):
        for y in dag[x]:
            src[y].add(x)
            tgt[x].add(y)
            if y in stack:
                stack.remove(y)
    while stack:
        x = stack.pop()
        yield x
        while tgt[x]:
            y = tgt[x].pop()
            src[y].remove(x)
            if src[y]:
                continue
            stack.add(y)


INF = 10 ** 9
n, m = map(int, input().split())
(*a,) = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
dp = [-INF] * n
min_dp = [INF] * n
for x in topological_sort(graph):
    min_dp[x] = min(min_dp[x], a[x])
    for y in graph[x]:
        dp[y] = max(dp[y], dp[x], a[y] - min_dp[x])
        min_dp[y] = min(min_dp[y], min_dp[x])
print(max(dp))
