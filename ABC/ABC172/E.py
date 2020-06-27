n, m = map(int, input().split())
p = 10**9 + 7
a = 1
fct = [a]
for i in range(1, m + 1):
    a = (a * i) % p
    fct.append(a)
b = pow(fct[-1], p - 2, p)
inv = [b]
for i in range(1, m + 1)[::-1]:
    b = (b * i) % p
    inv.append(b)
inv.reverse()
ans = (fct[m] * inv[m - n]) % p

tmp = 0
for i in range(1, n + 1):
    tmp += ((-1)**(i - 1) * fct[n] * inv[n - i] *
            inv[i] * fct[m - i] * inv[m - n]) % p
    tmp %= p
tmp = (fct[m] * inv[m - n] - tmp) % p
print((ans * tmp) % p)
