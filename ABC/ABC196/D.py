h, w, a, b = map(int, input().split())


def rec(a, b, bit):
    if bit == 0:
        return 1
    i = 0
    tmp = 1
    while not tmp & bit:
        i += 1
        tmp <<= 1
    res = 0
    if a > 0 and i % w != w - 1 and 1 << (i + 1) & bit:
        res += rec(a - 1, b, bit - (1 << i) - (1 << i + 1))
    if a > 0 and i // w != h - 1 and 1 << (i + w) & bit:
        res += rec(a - 1, b, bit - (1 << i) - (1 << i + w))
    if b > 0:
        res += rec(a, b - 1, bit - (1 << i))
    return res


print(rec(a, b, (1 << (h * w)) - 1))
