n, m = map(int, input().split())
G = [[] for i in range(n)]
I = [0 for i in range(n)]
for j in range(m):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    I[y-1] += 1
Q = [x for x in range(n) if I[x] == 0]
L = [0 for x in range(n)]
while Q:
    x = Q.pop()
    while G[x]:
        y = G[x].pop()
        I[y] -= 1
        L[y] = max(L[y], L[x]+1)
        if I[y] == 0:
            Q.append(y)
print(max(L))
