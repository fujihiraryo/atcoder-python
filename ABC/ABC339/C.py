n = int(input())
(*a,) = map(int, input().split())


def simulate(z):
    now = z
    for i in range(n):
        now += a[i]
        if now < 0:
            return -1
    return now


x, y = -1, 10**20
while y - x > 1:
    z = (x + y) // 2
    if simulate(z) == -1:
        x = z
    else:
        y = z
print(simulate(y))
