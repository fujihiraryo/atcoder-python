n, k = map(int, input().split())
(*A,) = map(int, input().split())
A.sort()
p = 10 ** 9 + 7
F, I = [1], [1]
for i in range(1, n + 1):
    F.append((F[-1] * i) % p)
    I.append((I[-1] * pow(i, p - 2, p)) % p)
s = 0
for i in range(k - 1, n):
    s += (A[i] - A[n - (i + 1)]) * F[i] * I[k - 1] * I[i - (k - 1)]
    s %= p
print(s)
