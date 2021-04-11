n, m = map(int, input().split())
y = pow(10, n, m)
z = pow(10, n, m ** 2)
if z < y:
    print(m + (z - y) // m)
else:
    print((z - y) // m)
