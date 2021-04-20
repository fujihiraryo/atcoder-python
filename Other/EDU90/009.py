import math
import bisect

INF = 1000
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
    args.append(INF)
    for j in range(n - 1):
        if args[j] > 180:
            break
        k = bisect.bisect_left(args, args[j] + 180)
        if abs(args[k - 1] - (args[j] + 180)) < abs(args[k] - (args[j] + 180)):
            k -= 1
        tmp = abs(args[j] - args[k])
        ans = max(ans, min(tmp, 360 - tmp))
print(ans)
