MOD = 10 ** 9 + 7
n = 10 ** 6 + 10
inv = [None]
for i in range(1, n):
    inv.append(pow(i, MOD - 2, MOD))


def cmb(x, y):
    ret = 1
    for i in range(y, 0, -1):
        ret = ret * (i - y + x) * inv[i] % MOD
    return ret


a, b, c, d = map(int, input().split())

ans = (
    cmb(c + d + 2, c + 1) - cmb(a + d + 1, a) - cmb(b + c + 1, c + 1) + cmb(a + b, a)
) % MOD
print(ans)
