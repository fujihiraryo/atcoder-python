def count2(n):
    # a*b<=nなる(a,b)の個数
    cnt = 0
    a = 1
    while a ** 2 < n:
        cnt += max(0, n // a - a)
        a += 1
    if a ** 2 > n:
        a -= 1
    return cnt * 2 + a


def test_count2(n):
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                cnt += 1
    return cnt


def count3(n):
    # a*b*c<=n
    cnt = 0
    for a in range(1, n + 1):
        cnt += count2(n // a)
    return cnt


def test_count3(n):
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i * j * k <= n:
                    cnt += 1
    return cnt


k = int(input())
print(count3(k))
