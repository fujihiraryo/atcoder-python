import math

t = int(input())
l, x, y = map(int, input().split())


def f(e):
    rad = math.radians(360 * e / t)
    y0 = -l / 2 * math.sin(rad)
    z0 = l / 2 - l / 2 * math.cos(rad)
    return math.degrees(math.atan2(z0, math.sqrt(x ** 2 + (y - y0) ** 2)))


q = int(input())
for _ in range(q):
    e = int(input())
    print(f(e))
