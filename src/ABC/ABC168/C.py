import numpy as np

a, b, h, m = map(int, input().split())
t = abs(6 * m - 30 * (h + m / 60))
t = min(360 - t, t)
t = np.deg2rad(t)
c = (a ** 2 + b ** 2 - 2 * a * b * np.cos(t)) ** 0.5
print(c)
