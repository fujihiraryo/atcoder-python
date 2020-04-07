n, m = map(int, input().split())
inf = 10**10
G = [{} for i in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    G[l-1][r-1] = d
    G[r-1][l-1] = -d
V = [False for i in range(n)]
D = [inf for i in range(n)]
for i in range(n):
    if V[i]:
        continue
    Q = [i]
    D[i] = 0
    while Q:
        j = Q.pop()
        V[j] = True
        for k in G[j].keys():
            if not V[k]:
                Q.append(k)
            if D[k] == inf:
                D[k] = D[j]+G[j][k]
            elif D[k] != D[j]+G[j][k]:
                print('No')
                exit()
print('Yes')
