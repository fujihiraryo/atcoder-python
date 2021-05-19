n, q = map(int, input().split())
*a, = map(int, input().split())
cur = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    x, y = (x - 1 - cur) % n, (y - 1 - cur) % n
    if t == 1:
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        cur += 1
    else:
        print(a[x])
