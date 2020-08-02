from itertools import product
n = int(input())
XYP = [tuple(map(int, input().split())) for i in range(n)]
X = [x for x, y, p in XYP]
Y = [y for x, y, p in XYP]
P = [p for x, y, p in XYP]
A = [1 << 30] * (n + 1)
for s in product(range(3), repeat=n):
    c = s.count(1) + s.count(2)
    d = 0
    for i in range(n):
        di = min(abs(X[i]), abs(Y[i])) * P[i]
        for j in range(n):
            if s[j] == 1:
                di = min(di, abs(X[i] - X[j]) * P[i])
            if s[j] == 2:
                di = min(di, abs(Y[i] - Y[j]) * P[i])
        d += di
    A[c] = min(A[c], d)
print(*A, sep="\n")
