n = int(input())
X, Y, P = [], [], []
for i in range(n):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

DX = [[0] * n for s in range(1 << n)]
DY = [[0] * n for s in range(1 << n)]
for s in range(1 << n):
    for i in range(n):
        DX[s][i] = abs(X[i]) * P[i]
        DY[s][i] = abs(Y[i]) * P[i]
        for j in range(n):
            if s & (1 << j):
                DX[s][i] = min(DX[s][i], abs(X[i] - X[j]) * P[i])
                DY[s][i] = min(DY[s][i], abs(Y[i] - Y[j]) * P[i])

A = [10**20] * (n + 1)
for sx in range(1 << n):
    rx = ((1 << n) - 1) ^ sx
    sy = rx
    while sy >= 0:
        sy &= rx
        d = 0
        for i in range(n):
            d += min(DX[sx][i], DY[sy][i])
        c = bin(sx).count("1") + bin(sy).count("1")
        A[c] = min(A[c], d)
        sy -= 1
print(*A, sep="\n")
