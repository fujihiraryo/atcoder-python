mod = 998244353
n, m, k = map(int, input().split())
if n > m:
    n, m = m, n
if n == 1:
    print(pow(k, m, mod))
else:
    ans = 0
    for x in range(1, k + 1):
        a = pow(x, n, mod) - pow(x - 1, n, mod)
        b = pow(k - x + 1, m, mod)
        ans += a * b
        ans %= mod
    print(ans)
