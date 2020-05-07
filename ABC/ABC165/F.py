import bisect
n = int(input())
*A, = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)
inf = 10**10
DP = [inf for i in range(n)]
L = [0 for i in range(n)]
V = [False for i in range(n)]
Q = [(0, -1)]
while Q:
    x, a = Q.pop()
    if a == -1:
        V[x] = True
        i = bisect.bisect_left(DP, A[x])
        Q.append((i, DP[i]))
        DP[i] = A[x]
        L[x] = bisect.bisect_left(DP, inf)
        for y in G[x]:
            if not V[y]:
                Q.append((y, -1))
    else:
        DP[x] = a
print(*L, sep='\n')
