h, w, d = map(int, input().split())
X = [None for k in range(h*w)]
for i in range(h):
    *A, = map(int, input().split())
    for j in range(w):
        X[A[j]-1] = (i, j)
D = []
for k in range(h*w):
    if k < d:
        D.append(0)
    else:
        x0, y0 = X[k]
        x1, y1 = X[k-d]
        D.append(D[k-d]+abs(x0-x1)+abs(y0-y1))
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(D[r-1]-D[l-1])
