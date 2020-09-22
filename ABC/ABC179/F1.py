n, q = map(int, input().split())
n -= 2
R, C = [None] * n, [None] * n
h, w = n, n
a = n**2
for _ in range(q):
    t, x = map(int, input().split())
    x -= 2
    if t == 1:
        for i in range(x, h):
            R[i] = w
        h = min(h, x)
        a -= R[x]
    if t == 2:
        for j in range(x, w):
            C[j] = h
        w = min(w, x)
        a -= C[x]
print(a)
