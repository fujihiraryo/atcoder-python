n, q = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
C = [0 for i in range(n)]
for j in range(q):
    p, x = map(int, input().split())
    C[p-1] += x
s = 0
Q = [s]
V = [False for i in range(n)]
while Q:
    x = Q.pop()
    V[x] = True
    for y in G[x]:
        if not V[y]:
            Q.append(y)
            C[y] += C[x]
print(*C)
