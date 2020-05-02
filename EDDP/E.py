n, m = map(int, input().split())
W, V = [], []
for i in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
sumV = sum(V)
A = [1 << 30 for j in range(sumV + 1)]
A[0] = 0
for i in range(n):
    B = []
    for j in range(V[i]):
        B.append(A[j])
    for j in range(V[i], sumV + 1):
        B.append(min(A[j], A[j - V[i]] + W[i]))
    A = B
for j in range(sumV, 0, -1):
    if A[j] <= m:
        print(j)
        exit()
