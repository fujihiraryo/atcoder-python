x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x, y = x0 - x1, y0 - y1
if x == 0 and y == 0:
    print(0)
elif x - y == 0 or x + y == 0 or abs(x) + abs(y) <= 3:
    print(1)
elif abs(x - y) <= 3 or abs(x + y) <= 3 or abs(x) + abs(y) <= 6 or (x - y) % 2 == 0:
    print(2)
else:
    print(3)
