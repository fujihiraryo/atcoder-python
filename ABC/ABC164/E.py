import heapq
inf = 10**20
h = 2500
n, m, s = map(int, input().split())
s = min(h-1, s)
# A[i][j]=iからjへの運賃
A = [[inf for j in range(n)] for i in range(n)]
# B[i][j]=iからjへの時間
B = [[inf for j in range(n)] for i in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    A[u-1][v-1] = a
    A[v-1][u-1] = a
    B[u-1][v-1] = b
    B[v-1][u-1] = b
CD = [tuple(map(int, input().split())) for i in range(n)]
# C[i]=iでの金貨の価値
C = [c for c, d in CD]
# D[i]=iでの両替時間
D = [d for c, d in CD]
# G[i,x][j,y]=状態(i,x)から(j,y)に変わるのにかかる時間
G = {(i, x): {} for i in range(n) for x in range(h)}
for i in range(n):
    for j in range(n):
        for x in range(h):
            if i == j:
                G[i, x][i, x] = 0
                if x-1 >= 0:
                    G[i, x][i, x-1] = 0
                if x+C[i] < h:
                    G[i, x][i, x+C[i]] = D[i]
            elif x >= A[i][j]:
                G[i, x][j, x-A[i][j]] = B[i][j]
# T[i,x]=状態(0,s)から(i,x)にかかる時間
T = {(i, x): inf for i in range(n) for x in range(h)}
T[0, s] = 0
Q = [(0, (0, s))]
heapq.heapify(Q)
while Q:
    _, (i, x) = heapq.heappop(Q)
    for j, y in G[i, x].keys():
        if T[i, x]+G[i, x][j, y] < T[j, y]:
            T[j, y] = T[i, x] + G[i, x][j, y]
            heapq.heappush(Q, (T[j, y], (j, y)))
for i in range(1, n):
    print(T[i, 0])
