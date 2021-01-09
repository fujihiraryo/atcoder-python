n, m = map(int, input().split())
graph = [{} for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c - 1
    graph[b - 1][a - 1] = c - 1
stack = [0]
ans = [None] * n
ans[0] = 0
for x in stack:
    for y in graph[x]:
        if ans[y] is not None:
            continue
        if ans[x] != graph[x][y]:
            ans[y] = graph[x][y]
        else:
            ans[y] = (graph[x][y] + 1) % n
        stack.append(y)
ans = [a + 1 for a in ans]
print(*ans, sep="\n")
