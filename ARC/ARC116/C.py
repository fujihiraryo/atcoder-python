from collections import defaultdict


class Sieve:
    def __init__(self, n):
        table = [i for i in range(n)]
        for i in range(2, n):
            if table[i] != i:
                continue
            for j in range(2 * i, n, i):
                table[j] = i
        self.table = table

    def factorize(self, x):
        y = x
        factor = defaultdict(int)
        while y > 1:
            factor[self.table[y]] += 1
            y //= self.table[y]
        return factor


MOD = 998244353
n, m = map(int, input().split())
fct, ict = [1], [1]
for i in range(1, n + m):
    fct.append(fct[-1] * i % MOD)
    ict.append(ict[-1] * pow(i, MOD - 2, MOD) % MOD)
sieve = Sieve(m + 1)
ans = 0
for x in range(1, m + 1):
    tmp = 1
    for i in sieve.factorize(x).values():
        tmp = tmp * fct[n - 1 + i] * ict[i] * ict[n - 1] % MOD
    ans = (ans + tmp) % MOD
print(ans)
