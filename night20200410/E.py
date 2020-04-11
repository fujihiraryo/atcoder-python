def dijkstra(G, s):
    # sを始点としてすべての点への最短距離を求める
    inf = 10**18
    n = len(G)
    D = [inf for i in range(n)]
    D[s] = 0
    Q = [s]
    while Q:
        x = Q.pop()
        for y in G[x]:
            if D[y] > D[x] + 1:
                D[y] = D[x] + 1
                Q.append(y)
    return D


n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
D0 = dijkstra(G, 0)
D1 = dijkstra(G, n-1)
c0, c1 = 0, 0
for i in range(n):
    if D0[i] <= D1[i]:
        c0 += 1
    else:
        c1 += 1
if c0 > c1:
    print('Fennec')
else:
    print('Snuke')
