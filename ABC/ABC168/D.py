import heapq

n, m = map(int, input().split())
G = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
inf = 10 ** 20
D = [inf for i in range(n)]
D[0] = 0
M = [None for i in range(n)]
Q = [(0, 0)]
heapq.heapify(Q)
while Q:
    _, x = heapq.heappop(Q)
    for y in G[x]:
        if D[x] + 1 < D[y]:
            D[y] = D[x] + 1
            M[y] = x
            heapq.heappush(Q, (D[y], y))
print("Yes")
for i in range(1, n):
    print(M[i] + 1)
