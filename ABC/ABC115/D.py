n, x = map(int, input().split())
ls, ss = [1], [1]
for i in range(1, n + 1):
    ls.append(ls[-1] * 2 + 3)
    ss.append(ss[-1] * 2 + 1)


def rec(n, x):
    if n == 0:
        return int(x > 0)
    if x <= 1 + ls[n - 1]:
        return rec(n - 1, x - 1)
    else:
        return ss[n - 1] + 1 + rec(n - 1, x - (ls[n - 1] + 2))


print(rec(n, x))
