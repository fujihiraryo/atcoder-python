# ARC034
def factrize(x):
    # 試し割りによるxの素因数分解
    f = {}
    tmp = x
    i = 2
    while i**2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp = tmp // i
        if cnt > 0:
            f[i] = cnt
        i += 1
    if tmp != 1 or f == {}:
        f[tmp] = 1
    return f


a, b = map(int, input().split())
F = {}
for n in range(b + 1, a + 1):
    f = factrize(n)
    for p in f:
        try:
            F[p] += f[p]
        except KeyError:
            F[p] = f[p]
ans = 1
mod = 10**9 + 7
for p in F:
    ans *= F[p] + 1
    ans %= mod
print(ans)
