import bisect
n, q = map(int, input().split())
STX = []
for i in range(n):
    s, t, x = map(int, input().split())
    STX.append((s, t, x))
STX.sort(key=lambda _: _[2])
S, T, X = [], [], []
for stx in STX:
    s, t, x = stx
    S.append(s)
    T.append(t)
    X.append(x)
D = [int(input()) for j in range(q)]
A = [-1 for j in range(q)]
B = [-1 for j in range(q)]
for i in range(n):
    l = bisect.bisect_left(D, S[i]-X[i])
    r = bisect.bisect_left(D, T[i]-X[i])
    while l < r:
        if B[l] == -1:
            A[l] = X[i]
            B[l] = r
            l += 1
        else:
            l = B[l]
print(*A, sep='\n')
