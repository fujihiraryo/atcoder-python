r, x, y = map(int, input().split())
r2 = pow(r, 2)
d2 = pow(x, 2) + pow(y, 2)
if d2 < r2:
    print(2)
    exit()
n = 0
while d2 > r2 * pow(n, 2):
    n += 1
print(n)
