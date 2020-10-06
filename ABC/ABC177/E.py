class Sieve:
    # エラトステネスの篩
    def __init__(self, n):
        # f[x]=0ならxは素数
        # f[x]はxの最小の素因数
        X = list(range(2, n + 1))
        f = {}
        while X[0] ** 2 <= n:
            tmp = X[0]
            f[tmp] = 0
            X_new = []
            for x in X[1:]:
                if x % tmp == 0:
                    f[x] = tmp
                else:
                    X_new.append(x)
            X = X_new
        for x in X:
            f[x] = 0
        self.primes = f

    def factrize(self, x):
        # n未満のxを素因数分解
        f = self.primes
        tmp = x
        g = {}
        while f[tmp]:
            try:
                g[f[tmp]] += 1
            except BaseException:
                g[f[tmp]] = 1
            tmp = tmp // f[tmp]
        try:
            g[tmp] += 1
        except BaseException:
            g[tmp] = 1
        return g


n = int(input())
(*A,) = map(int, input().split())
sieve = Sieve(10 ** 6)
P = {p: 0 for p in sieve.primes.keys() if sieve.primes[p] == 0}
for a in A:
    for p in sieve.factrize(a).keys():
        P[p] += 1
score = max(P.values())
if score == 1:
    print("pairwise coprime")
elif score != n:
    print("setwise coprime")
else:
    print("not coprime")
