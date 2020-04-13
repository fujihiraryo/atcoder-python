n, m = map(int, input().split())
inf = 10**10
# G[i][j] = iからjへの距離
G = [{} for i in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    G[l-1][r-1] = d
    G[r-1][l-1] = -d
# D[j] = jの属する連結成分のトップからjへの距離
D = [inf for i in range(n)]
# まだ探索していないiをトップとして探索する
for i in range(n):
    if D[i] != inf:
        continue
    Q = [i]
    D[i] = 0
    while Q:
        j = Q.pop()
        for k in G[j].keys():
            if D[k] == inf:
                Q.append(k)
            if D[k] == inf:
                D[k] = D[j]+G[j][k]
            elif D[k] != D[j]+G[j][k]:
                print('No')
                exit()
print('Yes')
