n = int(input())
X, Y, P = [], [], []
for i in range(n):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

DX = [[0] * n for s in range(2**n)]
DY = [[0] * n for s in range(2**n)]
for s in range(2**n):
    for i in range(n):
        DX[s][i] = abs(X[i]) * P[i]
        DY[s][i] = abs(Y[i]) * P[i]
        for j in range(n):
            if s & (1 << j):
                DX[s][i] = min(DX[s][i], abs(X[i] - X[j]) * P[i])
                DY[s][i] = min(DY[s][i], abs(Y[i] - Y[j]) * P[i])

A = [10**20] * (n + 1)
for s in range(3**n):
    tmp = s
    c, sx, sy = 0, 0, 0
    for i in range(n):
        if tmp % 3 != 0:
            c += 1
        if tmp % 3 == 1:
            sx += 2**i
        if tmp % 3 == 2:
            sy += 2**i
        tmp //= 3
    d = 0
    for i in range(n):
        d += min(DX[sx][i], DY[sy][i])
    A[c] = min(A[c], d)
print(*A, sep="\n")
