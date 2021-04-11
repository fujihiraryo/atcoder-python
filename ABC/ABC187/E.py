n = int(input())
graph = [set() for _ in range(n)]
edge = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].add(b)
    graph[b].add(a)
    edge.append((a, b))
# 根付き木の構成
que = [0]
visited = [0] * n
parent = [None] * n
while que:
    a = que.pop()
    visited[a] = 1
    for b in graph[a]:
        if visited[b]:
            continue
        que.append(b)
        parent[b] = a
# 各頂点に整数を置く
c = [0] * n
for _ in range(int(input())):
    t, e, x = map(int, input().split())
    a, b = edge[e - 1]
    if t == 2:
        a, b = b, a
    if a == parent[b]:
        c[0] += x
        c[b] -= x
    else:
        c[a] += x
# 根から順に累積和をとる
que = [0]
visited = [0] * n
while que:
    a = que.pop()
    visited[a] = 1
    for b in graph[a]:
        if visited[b]:
            continue
        que.append(b)
        c[b] += c[a]
print(*c, sep="\n")
