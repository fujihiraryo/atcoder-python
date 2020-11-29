a, b, x, y = map(int, input().split())
if a <= b:
    print(min(x + (b - a) * y, (2 * (b - a) + 1) * x))
else:
    print(min(x + (a - b - 1) * y, (2 * (a - b) - 1) * x))
