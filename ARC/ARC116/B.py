MOD = 998244353
inv2 = pow(2, MOD - 2, MOD)
n = int(input())
(*a,) = map(int, input().split())
a.sort()
s = [0]
for i in range(n):
    s.append((s[-1] + a[i] * pow(2, i, MOD)) % MOD)
ans = 0
for i in range(n):
    ans += pow(a[i], 2, MOD) % MOD
    ans %= MOD
tmp = 1
for i in range(n):
    tmp = tmp * inv2 % MOD
    ans += a[i] * tmp * (s[n] - s[i + 1]) % MOD
    ans %= MOD
print(ans)
