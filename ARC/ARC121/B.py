from bisect import bisect

INF = 10 ** 20
n = int(input())
r, g, b = [], [], []
for _ in range(2 * n):
    a, c = input().split()
    a = int(a)
    if c == "R":
        r.append(a)
    if c == "G":
        g.append(a)
    if c == "B":
        b.append(a)

r.append(INF)
g.append(INF)
b.append(INF)
r.append(-INF)
g.append(-INF)
b.append(-INF)
r.sort()
g.sort()
b.sort()


def matching(a, b):
    res = INF
    for x in a[1:-1]:
        i = bisect(b, x)
        res = min(res, min(x - b[i - 1], b[i] - x))
    return res


if len(r) % 2 == 0 and len(g) % 2 == 0 and len(b) % 2 == 0:
    ans = 0
if len(r) % 2 == 0 and len(g) % 2 == 1 and len(b) % 2 == 1:
    ans0 = matching(g, b)
    ans1 = matching(r, g) + matching(r, b)
    ans = min(ans0, ans1)
if len(r) % 2 == 1 and len(g) % 2 == 0 and len(b) % 2 == 1:
    ans0 = matching(r, b)
    ans1 = matching(r, g) + matching(g, b)
    ans = min(ans0, ans1)
if len(r) % 2 == 1 and len(g) % 2 == 1 and len(b) % 2 == 0:
    ans0 = matching(r, g)
    ans1 = matching(r, b) + matching(b, g)
    ans = min(ans0, ans1)
print(ans)
