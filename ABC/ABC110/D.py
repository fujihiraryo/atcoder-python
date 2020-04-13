def factrize(x):
    f = {}
    if x == 1:
        return f
    tmp = x
    i = 2
    while i**2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp = tmp//i
        if cnt > 0:
            f[i] = cnt
        i += 1
    if tmp != 1 or f == {}:
        f[tmp] = 1
    return f


def comb(n, r, p):
    x = 1
    for i in range(1, r + 1):
        x *= (n - i + 1) * pow(i, p - 2, p) % p
    return x % p


p = 10**9+7
n, m = map(int, input().split())
A = list(factrize(m).values())
ans = 1
for a in A:
    ans = (ans*comb(a+n-1, a, p)) % p
print(ans)
