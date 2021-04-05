def gcd(a, b):
    x, y = a, b
    while x:
        x, y = y % x, x
    return y


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
ans = 1
for _ in range(n):
    t = int(input())
    ans = lcm(ans, t)
print(ans)
