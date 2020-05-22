import bisect
INF = 10**9 + 1
n, m = map(int, input().split())
X, Y = [-INF, 0, INF], [-INF, 0, INF]
ABC, DEF = [], []
for i in range(n):
    a, b, c = map(int, input().split())
    ABC.append((a, b, c))
    X.append(a)
    X.append(b)
    Y.append(c)
    Y.append(c)
for j in range(m):
    d, e, f = map(int, input().split())
    DEF.append((d, e, f))
    X.append(d)
    X.append(d)
    Y.append(e)
    Y.append(f)
X.sort()
Y.sort()
V = [[0 for y in Y] for x in X]
for a, b, c in ABC:
    j = bisect.bisect_left(Y, c)
    ia = bisect.bisect_left(X, a)
    ib = bisect.bisect_left(X, b)
    for i in range(ia, ib):
        V[i][j] = 1
for d, e, f in DEF:
    i = bisect.bisect_left(X, d)
    je = bisect.bisect_left(Y, e)
    jf = bisect.bisect_left(Y, f)
    for j in range(je, jf):
        V[i][j] = 1
i = bisect.bisect_left(X, 0)
j = bisect.bisect_left(Y, 0)
Q = [(i, j)]
V[i][j] = 1
ans = 0
while Q:
    i, j = Q.pop()
    ans += (X[i + 1] - X[i]) * (Y[j + 1] - Y[j])
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 < i + di < len(X) - 1 and 0 < j + dj < len(Y) - 1:
            if V[i + di][j + dj] == 0:
                V[i + di][j + dj] = 1
                Q.append((i + di, j + dj))
        else:
            print('INF')
            exit()
print(ans)
