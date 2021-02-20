n, k = map(int, input().split())


def g1(x):
    lst = [int(c) for c in str(x)]
    lst.sort()
    lst = [str(c) for c in lst]
    return int("".join(lst))


def g2(x):
    lst = [int(c) for c in str(x)]
    lst.sort()
    lst.reverse()
    lst = [str(c) for c in lst]
    return int("".join(lst))


def f(x):
    return g2(x) - g1(x)


a = n
for i in range(k):
    a = f(a)
print(a)
