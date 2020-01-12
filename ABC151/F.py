import numpy as np
N = int(input())
P = []
for n in range(N):
    x, y = map(int, input().split())
    P.append((x, y))


def dist(p0, p1):
    x0, y0, x1, y1 = p0[0], p0[1], p1[0], p1[1]
    return (x0 - x1) ** 2 + (y0 - y1) ** 2


def f(x, y):
    return max([dist(p, (x, y)) for p in P])


def minfx(y):
    left = 0
    right = 1000
    for _ in range(80):
        left_ = left * (2 / 3) + right * (1 / 3)
        right_ = left*(1/3)+right*(2/3)
        if f(left_, y) <= f(right_, y):
            right = right_
        else:
            left = left_
    x0 = (left + right) / 2
    return f(x0, y)


left = 0
right = 1000
for _ in range(80):
    left_ = left * (2 / 3) + right * (1 / 3)
    right_ = left*(1/3)+right*(2/3)
    if minfx(left_) <= minfx(right_):
        right = right_
    else:
        left = left_
y0 = (left + right) / 2
print(np.sqrt(minfx(y0)))
