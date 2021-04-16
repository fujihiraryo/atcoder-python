MOD = 10 ** 9 + 7
n = int(input())
fct, ict = [1] * (n + 1), [1] * (n + 1)
for i in range(1, n + 1):
    fct[i] = fct[i - 1] * i % MOD
    ict[i] = ict[i - 1] * pow(i, MOD - 2, MOD) % MOD
cmb = lambda x, y: fct[x] * ict[y] * ict[x - y] % MOD
for k in range(1, n + 1):
    ans = 0
    for a in range(1, n + 1):
        if n < (k - 1) * (a - 1) + a:
            break
        ans += cmb(n - (k - 1) * (a - 1), a)
        ans %= MOD
    print(ans)
