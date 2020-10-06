N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = A[::-1]
p = 10 ** 9 + 7

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % p)
    inverse.append((-inverse[p % i] * (p // i)) % p)
    g2.append((g2[-1] * inverse[-1]) % p)


def cmb(n, r, p):
    if r < 0 or r > n:
        return 0
    return g1[n] * g2[r] * g2[n - r] % p


ans = 0
for n in range(N - K + 1):
    ans -= A[n] * cmb(N - n - 1, K - 1, p) % p
    ans += B[n] * cmb(N - n - 1, K - 1, p) % p
print(ans % p)
