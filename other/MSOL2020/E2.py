from itertools import product

n = int(input())
XYP = [tuple(map(int, input().split())) for i in range(n)]
X = [x for x, y, p in XYP]
Y = [y for x, y, p in XYP]
P = [p for x, y, p in XYP]

DX = {s: [0] * n for s in product(range(2), repeat=n)}
DY = {s: [0] * n for s in product(range(2), repeat=n)}
for s in product(range(2), repeat=n):
    for i in range(n):
        DX[s][i] = abs(X[i]) * P[i]
        DY[s][i] = abs(Y[i]) * P[i]
        for j in range(n):
            if s[j] == 1:
                DX[s][i] = min(DX[s][i], abs(X[i] - X[j]) * P[i])
                DY[s][i] = min(DY[s][i], abs(Y[i] - Y[j]) * P[i])

A = [1 << 40] * (n + 1)
for s in product(range(3), repeat=n):
    c = s.count(1) + s.count(2)
    sx = tuple((int(s[i] == 1) for i in range(n)))
    sy = tuple((int(s[i] == 2) for i in range(n)))
    A[c] = min(A[c], sum([min(DX[sx][i], DY[sy][i]) for i in range(n)]))
print(*A, sep="\n")
