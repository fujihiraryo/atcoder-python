MOD = 10 ** 9 + 7
k = int(input())
s = input()
n = len(s)
fct, ict = [1], [1]
pow25, pow26 = [1], [1]
for i in range(1, n + k):
    fct.append(fct[-1] * i % MOD)
    ict.append(ict[-1] * pow(i, MOD - 2, MOD) % MOD)
    pow25.append(pow25[-1] * 25 % MOD)
    pow26.append(pow26[-1] * 26 % MOD)
ans = 0
for i in range(k + 1):
    ans += fct[i + n - 1] * ict[i] * ict[n - 1] * pow25[i] * pow26[k - i]
    ans %= MOD
print(ans)
