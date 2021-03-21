p = int(input())
(*a,) = map(int, input().split())
c = [[0] * p for _ in range(p)]
c[0][0] = 1
for i in range(1, p):
    c[i][0] = 1
    for j in range(1, p):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % p
b = [0] * p
for i in range(p):
    s = sum(a[j] * pow(-j, p - 1 - i, p) for j in range(p))
    b[i] = (p - 1) * c[p - 1][i] * s % p
b[0] = (b[0] + sum(a)) % p
print(*b)
