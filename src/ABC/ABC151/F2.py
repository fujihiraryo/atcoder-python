def dist2(a, b):
    # 2点a,bの距離の2乗
    ax, ay = a
    bx, by = b
    return (ax - bx) ** 2 + (ay - by) ** 2


def circum(a, b, c):
    # 三角形ABCの外心
    ax, ay = a
    bx, by = b
    cx, cy = c
    s = dist2(b, c) * (dist2(c, a) + dist2(a, b) - dist2(b, c))
    t = dist2(c, a) * (dist2(a, b) + dist2(b, c) - dist2(c, a))
    u = dist2(a, b) * (dist2(b, c) + dist2(c, a) - dist2(a, b))
    ox = (s * ax + t * bx + u * cx) / (s + t + u)
    oy = (s * ay + t * by + u * cy) / (s + t + u)
    return ox, oy


n = int(input())
P = [tuple(map(int, input().split())) for i in range(n)]
eps = 10 ** (-7)
if n == 2:
    r = dist2(P[0], P[1]) ** 0.5 / 2
    print(r)
    exit()
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b, c = P[i], P[j], P[k]
            ax, ay = a
            bx, by = b
            cx, cy = c
            if dist2(a, b) + dist2(b, c) <= dist2(c, a):
                p = (cx + ax) / 2, (cy + ay) / 2
                r2 = dist2(a, p)
            elif dist2(b, c) + dist2(c, a) <= dist2(a, b):
                p = (ax + bx) / 2, (ay + by) / 2
                r2 = dist2(b, p)
            elif dist2(c, a) + dist2(a, b) <= dist2(b, c):
                p = (bx + cx) / 2, (by + cy) / 2
                r2 = dist2(c, p)
            else:
                p = circum(a, b, c)
                r2 = dist2(a, p)
            if all([dist2(p, q) <= r2 + eps for q in P]):
                print(r2 ** 0.5)
                exit()
