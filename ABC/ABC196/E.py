INF = 1 << 64
n = int(input())
a, b, c = 0, -INF, INF
for _ in range(n):
    p, t = map(int, input().split())
    if t == 1:
        ai, bi, ci = p, -INF, INF
    if t == 2:
        ai, bi, ci = 0, p, INF
    if t == 3:
        ai, bi, ci = 0, -INF, p
    a = a + ai
    b = max((b + ai), bi)
    c = min(max((c + ai), bi), ci)
input()
for x in map(int, input().split()):
    print(min(max(x + a, b), c))
