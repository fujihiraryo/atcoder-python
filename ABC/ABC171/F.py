k = int(input())
n = len(input())
k, n = 10**6, 10**6
p = 10**9 + 7
a = 1
fct = [a]
for i in range(1, n + k + 1):
    a = (a * i) % p
    fct.append(a)
b = pow(fct[-1], p - 2, p)
inv = [b]
for i in range(1, n + k + 1)[::-1]:
    b = (b * i) % p
    inv.append(b)
inv.reverse()
ans = 0
pow25, pow26 = [1], [1]
for i in range(1, k + 1):
    pow25.append((pow25[-1] * 25) % p)
    pow26.append((pow26[-1] * 26) % p)
for i in range(k + 1):
    c = fct[i + n - 1] * inv[i] * inv[n - 1]
    ans += pow25[i] * pow26[k - i] * c
    ans %= p
print(ans)
