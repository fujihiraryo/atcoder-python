def div(x):
    D = set()
    d = 1
    while d * d <= x:
        if x % d == 0:
            D.add(d)
            D.add(x // d)
        d += 1
    return D


n = int(input())
cnt = 0
for d in div(n) | div(n - 1):
    if d == 1:
        continue
    tmp = n
    while tmp % d == 0:
        tmp = tmp // d
    if tmp % d == 1:
        cnt += 1
print(cnt)
