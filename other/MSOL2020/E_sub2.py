n = int(input())
XP = [tuple(map(int, input().split())) for i in range(n)]
X = [x for x, p in XP]
P = [p for x, p in XP]
A = [1 << 30] * (n + 1)
for s in range(1 << n):
    c = bin(s).count("1")
    d = 0
    for i in range(n):
        di = abs(X[i] * P[i])
        for j in range(n):
            if (s >> j) & 1:
                di = min(di, abs(X[i] - X[j]) * P[i])
        d += di
    A[c] = min(A[c], d)
print(*A, sep="\n")
