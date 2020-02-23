"""
pが素数で、入力が
n r p
で与えられたときnCrをmod pで計算する
"""

n, r, p = 100, 50, 10**9+7


g1 = [1, 1]
g2 = [1, 1]

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % p)
    g2.append((g2[-1] * pow(i, p-2, p)) % p)


def cmb(n, r, p):
    if (r < 0 or r > n):
        return 0
    return g1[n] * g2[r] * g2[n-r] % p


print(cmb(n, r, p))
print(cmb(6, 3, p))
