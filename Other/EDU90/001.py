n, m = map(int, input().split())
k = int(input())
(*a,) = map(int, input().split())


def judge(x):
    t = 0
    i = 0
    for _ in range(k):
        for j in range(i, n):
            if a[j] - t >= x:
                break
        i = j
        t = a[j]
    return m - t >= x


x, y = 0, m
while y - x > 1:
    z = (x + y) // 2
    if judge(z):
        x = z
    else:
        y = z
print(x)
