MOD = 998244353
n = int(input())
inv_n = pow(n, MOD - 2, MOD)
x, y = 0, 0
k = 0
while k < n:
    k += 1
    p = k * inv_n % MOD
    q = (1 - k * inv_n) % MOD
    q2 = pow(q, 2, MOD)
    x0, y0 = x, y
    y = ((p * x0 + p * q * y0 + q2) % MOD) * pow(1 - q2, MOD - 2, MOD) % MOD
    x = (p * y0 + q * (y + 1)) % MOD
print(x, y)
