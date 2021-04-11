MOD = 10 ** 9 + 7
fct, ict = [1], [1]
for i in range(1, 2000):
    fct.append(fct[-1] * i % MOD)
    ict.append(ict[-1] * pow(i, MOD - 2, MOD) % MOD)
s = int(input())
n = 1
ans = 0
while 3 * n <= s:
    ans += fct[s - 2 * n - 1] * ict[n - 1] * ict[s - 3 * n]
    ans %= MOD
    n += 1
print(ans)
