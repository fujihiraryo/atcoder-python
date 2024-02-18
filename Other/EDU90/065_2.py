MOD = 998244353
n = 10**6

inv = [None] * (n + 1)
inv[1] = 1
for i in range(2, n + 1):
    inv[i] = -(MOD // i) * inv[MOD % i] % MOD

fct = [1] * (n + 1)
ifc = [1] * (n + 1)
for i in range(1, n + 1):
    fct[i] = fct[i - 1] * i % MOD
    ifc[i] = ifc[i - 1] * inv[i] % MOD


def cmb(x, y):
    if x < y or x < 0 or y < 0:
        return 0
    else:
        return fct[x] * ifc[x - y] * ifc[y] % MOD


r, g, b, k = map(int, input().split())
x, y, z = map(int, input().split())
ans = 0
for cr in range(r + 1):
    for cg in range(g + 1):
        if cr + cg > k:
            continue
        cb = k - cr - cg
        if cb > b:
            continue
        if cr + cg > x or cg + cb > y or cb + cr > z:
            continue
        ans += cmb(r, cr) * cmb(g, cg) * cmb(b, cb)
        ans %= MOD
print(ans)
