import math


def rotate(x, y, theta):
    cos = math.cos(theta)
    sin = math.sin(theta)
    return x * cos - y * sin, x * sin + y * cos


n = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = (x0 + x1) / 2, (y0 + y1) / 2
x3, y3 = rotate(x0 - x2, y0 - y2, 2 * math.pi / n)
print(x2 + x3, y2 + y3)
