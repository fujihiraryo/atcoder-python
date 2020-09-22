n, x, m = map(int, input().split())
a = x
S = [0] * (m + 1)
F = [None] * m
F[x] = 0
i0, j0 = None, None
for i in range(1, m + 1):
    S[i] = S[i - 1] + a
    a = pow(a, 2, m)
    if F[a] is not None:
        i0, j0 = F[a], i
    F[a] = i
q, r = (n - i0) // (j0 - i0), (n - i0) % (j0 - i0)
print((S[j0] - S[i0]) * q + S[i0 + r])
