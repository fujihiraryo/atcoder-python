n, m, k = map(int, input().split())
p = 998244353
fct, inv = [1], [1]
for i in range(1, n):
    fct.append((fct[-1] * i) % p)
    inv.append((inv[-1] * pow(i, p - 2, p)) % p)
ans = 0
for i in range(k + 1):
    cmb = fct[n - 1] * inv[i] * inv[n - 1 - i]
    ans = (ans + cmb * m * pow(m - 1, n - 1 - i, p)) % p
print(ans)
