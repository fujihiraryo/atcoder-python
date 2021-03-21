from itertools import combinations

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
for i in range(n):
    graph[i][i] = 1
s = set(range(n))
cnt = 0
while s:
    max_clique = {list(s)[0]}
    for i in range(len(s) + 1):
        for t in combinations(s, i):
            if all(graph[x][y] for x, y in combinations(t, 2)):
                max_clique = set(t)
    s -= max_clique
    cnt += 1
print(cnt)
