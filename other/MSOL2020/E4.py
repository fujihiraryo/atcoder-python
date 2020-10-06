from itertools import product

n = int(input())
XYP = [tuple(map(int, input().split())) for i in range(n)]
X = [x for x, y, p in XYP]
Y = [y for x, y, p in XYP]
P = [p for x, y, p in XYP]

DX = [[0] * n for s in range(2 ** n)]
DY = [[0] * n for s in range(2 ** n)]
for s in range(2 ** n):
    for i in range(n):
        DX[s][i] = abs(X[i]) * P[i]
        DY[s][i] = abs(Y[i]) * P[i]
        for j in range(n):
            if s & (1 << j):
                DX[s][i] = min(DX[s][i], abs(X[i] - X[j]) * P[i])
                DY[s][i] = min(DY[s][i], abs(Y[i] - Y[j]) * P[i])

pow2 = [2 ** i for i in range(n)]
A = [10 ** 20] * (n + 1)
for s in product(range(3), repeat=n):
    tmp = s
    # c, sx, sy = 0, 0, 0
    # for i in range(n):
    #     if tmp % 3 == 1:
    #         sx += pow2[i]
    #         c += 1
    #     if tmp % 3 == 2:
    #         sy += pow2[i]
    #         c += 1
    #     tmp //= 3
    c, sx, sy = 0, 0, 0
    for i in range(n)[::-1]:
        if s[i] == 1:
            sx += pow2[i]
            c += 1
        if s[i] == 2:
            sy += pow2[i]
            c += 1
    d = 0
    for i in range(n):
        d += min(DX[sx][i], DY[sy][i])
    A[c] = min(A[c], d)
    # A[c] = min(A[c], sum(min(DX[sx][i], DY[sy][i]) for i in range(n)))
print(*A, sep="\n")
