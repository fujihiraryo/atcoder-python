import math
import bisect

n = int(input())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
ans = 0
for i in range(n):
    args = []
    for j in range(n):
        if i == j:
            continue
        rad = math.atan2(y[j] - y[i], x[j] - x[i])
        deg = math.degrees(rad)
        if deg < 0:
            deg += 360
        args.append(deg)
    args.sort()
    args.append(360)
    for j in range(n - 1):
        if args[j] > 180:
            break
        k = bisect.bisect_left(args, args[j] + 180)
        t0 = abs(args[j] - args[k])
        t1 = abs(args[j] - args[k - 1])
        t = min(t0, t1)
        ans = max(ans, min(t, 360 - t))
print(ans)
