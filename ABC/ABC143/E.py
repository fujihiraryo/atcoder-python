def warshall_floyd(G):
    inf = 10**18
    # 重みつきグラフGに対してすべての頂点対の距離を求める
    n = len(G)
    d = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][i] = 0
        for j in G[i].keys():
            d[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d


n, m, l = map(int, input().split())
G = [{} for i in range(n)]
for j in range(m):
    a, b, c = map(int, input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c
D = warshall_floyd(G)
G = [{} for i in range(n)]
for i in range(n):
    for j in range(n):
        if D[i][j] <= l:
            G[i][j] = 1
D = warshall_floyd(G)
for k in range(int(input())):
    s, t = map(int, input().split())
    if D[s-1][t-1] > 10**10:
        print(-1)
    else:
        print(D[s-1][t-1]-1)
