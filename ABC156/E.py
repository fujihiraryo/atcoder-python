# min(n-1,k)以下の自然数mに対してnCm*n-1Cmの和を求める
n, k = map(int, input().split())
p = 10 ** 9 + 7
g1 = [1, 1]
g2 = [1, 1]

# 先にn!と(n!)^(-1)のリストを作っておく
for i in range(2, 2 * 10 ** 5 + 1):
    g1.append((g1[-1] * i) % p)
    g2.append((g2[-1] * pow(i, p-2, p)) % p)


def cmb(n, r):
    return g1[n] * g2[r] * g2[n - r] % p


ans = 0
for m in range(min(n - 1, k) + 1):
    ans += cmb(n, m) * cmb(n - 1, m) % p
print(ans % p)
