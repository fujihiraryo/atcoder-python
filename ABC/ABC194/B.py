n = int(input())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = 10 ** 30
for i in range(n):
    ans = min(ans, a[i] + b[i])
    for j in range(n):
        if i == j:
            continue
        ans = min(ans, max(a[i], b[j]))
print(ans)
