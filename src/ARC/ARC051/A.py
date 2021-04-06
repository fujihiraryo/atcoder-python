x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
red, blue = 0, 0
is_red = lambda x, y: (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2
is_blue = lambda x, y: x2 <= x <= x3 and y2 <= y <= y3
for x in range(-100, 100 + 1):
    for y in range(-100, 100 + 1):
        if is_red(x, y) and not is_blue(x, y):
            red = 1
        if not is_red(x, y) and is_blue(x, y):
            blue = 1
print("YES" if red else "NO")
print("YES" if blue else "NO")
