import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    L, R = [], []
    N = [[] for j in range(n)]
    P = [[] for j in range(n + 1)]
    for i in range(n):
        k, l, r = map(int, input().split())
        if l - r > 0:
            N[k - 1].append(i)
        else:
            P[k].append(i)
        L.append(l)
        R.append(r)
    ans = sum([min(L[i], R[i]) for i in range(n)])
    S, T = [], []
    for j in range(n):
        for i in N[j]:
            heapq.heappush(S, L[i] - R[i])
        for i in P[n - 1 - j]:
            heapq.heappush(T, R[i] - L[i])
        while len(S) > j + 1:
            heapq.heappop(S)
        while len(T) > j + 1:
            heapq.heappop(T)
    print(ans + sum(S) + sum(T))
