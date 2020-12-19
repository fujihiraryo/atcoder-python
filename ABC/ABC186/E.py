def ext_euclid(a, b):
    # 互いに素なa,bに対して、方程式ax+by=1の整数解を1つ求める
    x0, y0, r0 = 1, 0, a
    x1, y1, r1 = 0, 1, b
    while r0:
        x0, x1 = x1 - x0 * (r1 // r0), x0
        y0, y1 = y1 - y0 * (r1 // r0), y0
        r0, r1 = r1 % r0, r0
    return x1, y1, r1


t = int(input())
query = [map(int, input().split()) for _ in range(t)]
for n, s, k in query:
    _, _, r = ext_euclid(k, n)
    if s % r != 0:
        print(-1)
        continue
    a, b, c = k // r, n // r, (n - s) // r
    x, y, _ = ext_euclid(a, b)
    print(c * x % b)
