n = 300000
q = 300000
A = [1 << 30 for _ in range(n)]
query = [(1, i + 1, i + 1) for i in range(n)] + [(2, 1, n) for i in range(n)]
print(n, q)
print(*A)
for t, x, y in query:
    print(t, x, y)
