n, k = map(int, input().split())
a, b = [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
idx = list(range(n))
idx.sort(key=lambda i: a[i])
x = 0
for i in idx:
    if k >= a[i] - x:
        k -= a[i] - x
        x = a[i]
        k += b[i]
print(x + k)
