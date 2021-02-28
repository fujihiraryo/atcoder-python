def ext_euclid(a, b):
    x0, y0, r0 = 1, 0, a
    x1, y1, r1 = 0, 1, b
    while r0:
        x0, x1 = x1 - x0 * (r1 // r0), x0
        y0, y1 = y1 - y0 * (r1 // r0), y0
        r0, r1 = r1 % r0, r0
    return x1, y1, r1


def crt(m, r):
    # 各iでx%m[i]=r[i]となるxを求める
    m0, r0 = 1, 0
    for m1, r1 in zip(m, r):
        _, _, g = ext_euclid(m0, m1)
        if (r0 - r1) % g:
            return None
        x0, _, _ = ext_euclid(m0 // g, m1 // g)
        r0 = r0 + m0 * (r1 - r0) * x0 // g
        m0 = m0 * m1 // g
        r0 %= m0
    return r0


INF = 10 ** 30
t = int(input())
for _ in range(t):
    x, y, p, q = map(int, input().split())
    ans = INF
    for a in range(x, x + y):
        for b in range(p, p + q):
            m = [2 * (x + y), p + q]
            r = [a, b]
            tmp = crt(m, r)
            if tmp is None:
                continue
            ans = min(ans, tmp)
    print(ans if ans != INF else "infinity")
