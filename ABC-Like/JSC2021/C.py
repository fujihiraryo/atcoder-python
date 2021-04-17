def divisor(n):
    res = set()
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            res.add(i)
            res.add(n // i)
        i += 1
    return res


MAX = 2 * 10 ** 5
cnt = [0] * (MAX + 1)
a, b = map(int, input().split())
for i in range(a, b + 1):
    for x in divisor(i):
        cnt[x] += 1
for x in range(MAX + 1)[::-1]:
    if cnt[x] >= 2:
        print(x)
        exit()
