mod = 998244353
n = int(input())
rn = pow(n, mod - 2, mod)
(*a,) = map(int, input().split())
ans = 0
for i in range(n):
    p = rn * pow(1 + rn, i, mod) % mod
    ans += p * a[i]
    ans %= mod
print(ans)
