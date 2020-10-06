N, K = map(int, input().split())
G = [[] for n in range(N)]
for n in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# まず各部分木の根にカウンターを乗せる
C = [0] * N
for k in range(K):
    p, x = map(int, input().split())
    C[p - 1] += x

# 深さ優先探索で親のカウンターを子に継いでいく
V = [False] * N
Q = [0]
while Q:
    x = Q.pop()
    V[x] = True
    for y in G[x]:
        if not V[y]:
            C[y] += C[x]
            Q.append(y)
print(*C)
