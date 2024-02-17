n, m, k = map(int, input().split())
k -= 1


def gcd(a, b):
    x, y = a, b
    while x:
        x, y = y % x, x
    return y


lcm = n * m // gcd(n, m)
size = lcm // n - 1 + lcm // m - 1
cnt = k // size
res = k % size
# res番目の値+cnt*lcm
x = 0
y = lcm
while y - x > 1:
    z = (x + y) // 2
    if z // n + z // m >= res + 1:
        y = z
    else:
        x = z
print(y + cnt * lcm)
