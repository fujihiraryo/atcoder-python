mod = 10**9+7

X, Y = map(int, input().split())


def comb(n, r, mod):
    if r < 0 or n < r:
        return 0
    return fact[n]*pow(fact[r], mod-2, mod) * pow(fact[n-r], mod-2, mod) % mod


if (X + Y) % 3 != 0:
    ans = 0
else:
    n = (X + Y) // 3
    r = min(X, Y)-n
    # nCr
    fact = [1, 1]
    for i in range(2, n+1):
        fact.append(fact[-1] * i % mod)
    ans = comb(n, r, mod)

print(ans)
