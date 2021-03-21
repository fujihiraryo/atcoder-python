INF = 1 << 30


def merge(x, y):
    cnt = 0
    nx, ny = len(x), len(y)
    x.append(INF)
    y.append(INF)
    z = []
    i, j = 0, 0
    for k in range(nx + ny):
        if x[i] < y[j]:
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
(*a,) = map(int, input().split())
b = a[:]
_, ans = merge_sort(b)
for i in range(n):
    print(ans)
    ans -= a[i]
    ans += n - 1 - a[i]
