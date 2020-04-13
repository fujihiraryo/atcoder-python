class Comb():
    def __init__(self, n, p):
        # O(n)
        fct, inv = [1, 1], [1, 1]
        a, b = 1, 1
        for i in range(2, n + 1):
            a = (a * i) % p
            b = (b * pow(i, p - 2, p)) % p
            fct.append(a)
            inv.append(b)
        self.fct = fct
        self.inv = inv
        self.n = n
        self.p = p

    def calc(self, n, r):
        fct, inv = self.fct, self.inv
        if (r < 0 or n < r):
            return 0
        else:
            return fct[n] * inv[r] * inv[n - r] % p


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = A[::-1]
p = 10 ** 9 + 7
cmb = Comb(N, p)
ans = 0
for n in range(N - K + 1):
    c = cmb.calc(N - n - 1, K-1)
    ans -= A[n] * c % p
    ans += B[n] * c % p
print(ans % p)
