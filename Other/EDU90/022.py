def gcd(a, b):
    x, y = a, b
    while x:
        x, y = y % x, x
    return y


a, b, c = map(int, input().split())
g = gcd(gcd(a, b), c)
print((a - 1) // g + (b - 1) // g + (c - 1) // g)
