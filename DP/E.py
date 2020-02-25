inf = 10**10
N, M = map(int, input().split())
W, V = [], []
for n in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
X = sum(V)
f = [inf for x in range(X + 1)]
f[0] = 0
for n in range(N):
    f = [
        min(f[x], f[x - V[n]] + W[n]) if x >= V[n] else f[x]
        for x in range(X + 1)
    ]
for x in range(X + 1)[::-1]:
    if f[x] <= M:
        print(x)
        exit()
