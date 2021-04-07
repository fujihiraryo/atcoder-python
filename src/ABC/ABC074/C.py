a, b, c, d, e, f = map(int, input().split())
water_set = set()
sugar_set = set()
for i in range(3001):
    for j in range(3001):
        if 100 * (a * i + b * j) <= f:
            water_set.add(a * i + b * j)
        if c * i + d * j <= f:
            sugar_set.add(c * i + d * j)
x0, y0 = 1, 0
for x in water_set:
    for y in sugar_set:
        if 100 * x + y <= f and y <= e * x and x0 * y >= x * y0:
            x0, y0 = x, y
print(100 * x0 + y0, y0)
