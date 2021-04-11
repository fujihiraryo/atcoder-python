n, m, t = map(int, input().split())
x = n
s = 0
for _ in range(m):
    a, b = map(int, input().split())
    x -= a - s
    if x <= 0:
        print("No")
        exit()
    x += b - a
    x = min(n, x)
    s = b
x -= t - s
if x <= 0:
    print("No")
else:
    print("Yes")
