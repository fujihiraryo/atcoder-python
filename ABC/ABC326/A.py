x, y = map(int, input().split())
if y - x > 2 or x - y > 3:
    print("No")
else:
    print("Yes")
