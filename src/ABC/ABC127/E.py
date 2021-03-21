MOD = 10 ** 9 + 7
n, m, k = map(int, input().split())
fct, ifc = [1], [1]
for i in range(1, m * n):
    fct.append((fct[-1] * i) % MOD)
    ifc.append((ifc[-1] * pow(i, MOD - 2, MOD)) % MOD)
x = m ** 2 * n * (n ** 2 - 1) // 6
y = n ** 2 * m * (m ** 2 - 1) // 6
cmb = fct[m * n - 2] * ifc[k - 2] * ifc[m * n - k] % MOD
ans = (x + y) * cmb % MOD
print(ans)
