x, y, z = map(int, input().split())
if (y * z) % x:
    print((y * z) // x)
else:
    print((y * z) // x - 1)
