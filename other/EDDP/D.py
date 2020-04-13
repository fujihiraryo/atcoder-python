n, m = map(int, input().split())
W, V = [], []
for i in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
A = [0 for j in range(m+1)]
for i in range(n):
    B = []
    for j in range(W[i]):
        B.append(A[j])
    for j in range(W[i], m+1):
        B.append(max(A[j], A[j-W[i]]+V[i]))
    A = B
print(A[m])
