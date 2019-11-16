mod = 10**9+7
N = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    return g1[n] * g2[r] * g2[n-r] % mod


X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    ans = 0
else:
    n = (X + Y) // 3
    r = min(X, Y) - n
    ans = cmb(n, r, mod)
print(ans)
