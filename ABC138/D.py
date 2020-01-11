N, K = map(int, input().split())
G = [[] for n in range(N)]
for n in range(N-1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

C = [0] * N
for k in range(K):
    p, x = map(int, input().split())
    C[p - 1] += x

# 親情報の作成
P = [-1]*N
Q = [0]
X = []
count = 0
while Q:
    v = Q.pop()
    X.append(v)
    if v != 0:
        C[v] += C[P[v]]
    for u in G[v]:
        if u == P[v]:
            continue
        P[u] = v
        Q.append(u)

C = [str(c) for c in C]
print(" ".join(C))
