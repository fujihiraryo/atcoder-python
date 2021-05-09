k, n, m = map(int, input().split())
*a, = map(int, input().split())


def make(x):
    p = [max(0, -(-(m * a[i] - x) // n)) for i in range(k)]
    q = [(m * a[i] + x) // n for i in range(k)]
    if any(p[i] > q[i] for i in range(k)):
        return None
    b = p[:]
    t = sum(p)
    if t > m:
        return None
    for i in range(k):
        b[i] += min(m - t, q[i] - p[i])
        t += min(m - t, q[i] - p[i])
    if t == m:
        return b
    return None


x, y = 0, 10 ** 10
while y - x > 1:
    z = (x + y) // 2
    b = make(z)
    if b is None:
        x = z
    else:
        y = z
print(*make(y))
