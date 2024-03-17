def solve(a, p):
    n = sum(a)
    s = sum((i + 1) * a[i] for i in range(5))
    if 3 * n - s <= 0:
        return 0
    x0, y0 = 3 * n - s, 0
    x1, y1 = 0, -(-(3 * n - s) // 2)
    x2, y2 = 1, (3 * n - s) // 2
    return min(p[3] * x0 + p[4] * y0, p[3] * x1 + p[4] * y1, p[3] * x2 + p[4] * y2)


t = int(input())
for _ in range(t):
    (*a,) = map(int, input().split())
    (*p,) = map(int, input().split())
    print(solve(a, p))
