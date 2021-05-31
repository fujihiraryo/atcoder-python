INF = 1 << 30


def merge(x, y):
    cnt = 0
    nx, ny = len(x), len(y)
    x.append(INF)
    y.append(INF)
    z = []
    i, j = 0, 0
    for k in range(nx + ny):
        if x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
            cnt += nx - i
    return z, cnt


def merge_sort(a):
    n = len(a)
    if n == 1:
        return a, 0
    x, cnt_x = merge_sort(a[: n // 2])
    y, cnt_y = merge_sort(a[n // 2 :])
    a, cnt = merge(x, y)
    return a, cnt + cnt_x + cnt_y


n = int(input())
*a, = map(int, input().split())
l, r = 0, 10 ** 9
while r - l > 1:
    x = (l + r) // 2
    b = [int(a[i] <= x) for i in range(n)]
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + b[i]
    t = [i - 2 * s[i] for i in range(n + 1)]
    _, cnt = merge_sort(t)
    if cnt * 4 > n * (n + 1):
        r = x
    else:
        l = x
print(r)
