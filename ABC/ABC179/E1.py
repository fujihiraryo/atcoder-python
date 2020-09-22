n, x, m = map(int, input().split())
S = [0]
F = [None] * m
for j in range(m + 1):
    S.append(S[-1] + x)
    if F[x] is not None:
        i = F[x]
        q, r = (n - i) // (j - i), (n - i) % (j - i)
        print((S[j] - S[i]) * q + S[i + r])
        exit()
    F[x] = j
    x = pow(x, 2, m)
