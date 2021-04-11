n, x = map(int, input().split())
a, b, c = [], [], []
for _ in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
pv = []
for i in range(n):
    pv.append((a[i], c[i]))
    pv.append((b[i] + 1, -c[i]))
pv.sort()
m = len(pv)
ans = 0
s = 0
for i in range(m - 1):
    p0, v0 = pv[i]
    p1, v1 = pv[i + 1]
    s += v0
    ans += min(s, x) * (p1 - p0)
print(ans)
