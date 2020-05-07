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
Q = [(-1, 0, None)]
while Q:
    p, x, a = Q.pop()
    if x == -1:
        DP[p] = a
        continue
    i = bisect.bisect_left(DP, A[x])
    Q.append((i, -1, DP[i]))
    DP[i] = A[x]
    L[x] = bisect.bisect_left(DP, inf)
    for y in G[x]:
        if y != p:
            Q.append((x, y, None))
print(*L, sep='\n')
