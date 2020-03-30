def sieve(n):
    X = list(range(2, n + 1))
    # fは数字と最小の素因数の対応
    f = {}
    while X[0] <= n ** 0.5:
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
    return f


def factorize(n):
    # 素因数分解 6桁くらいまでは一瞬
    f = sieve(n)
    tmp = n
    g = {}
    while f[tmp]:
        try:
            g[f[tmp]] += 1
        except:
            g[f[tmp]] = 1
        tmp = tmp // f[tmp]
    try:
        g[tmp] += 1
    except:
        g[tmp] = 1
    return g


print(factorize(100331))
