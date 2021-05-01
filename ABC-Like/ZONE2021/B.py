n, d, h = map(int, input().split())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)


def check(a):
    for i in range(n):
        if d * y[i] >= (h - a) * x[i] + a * d:
            return False
    return True


a, b = 0, 1000
while b - a > 0.00001:
    c = (a + b) / 2
    if check(c):
        b = c
    else:
        a = c
print(c)
