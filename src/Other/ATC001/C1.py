class FFT:
    def __init__(self, n, p, w):
        # pは素数で, wは1のn乗根(mod p)
        # 例:(n,p,w)=(4,5,2),(8,17,2),(262144,1541406721,103)
        self.n = n
        self.p = p
        self.w = w
        self.rn = pow(n, p - 2, p)
        self.rw = pow(w, p - 2, p)

    def base(self, A, n, w):
        p = self.p
        for i in range(n - len(A)):
            A.append(0)
        if n == 1:
            return A
        F0 = self.base(A[0::2], n // 2, pow(w, 2, p))
        F1 = self.base(A[1::2], n // 2, pow(w, 2, p))
        x = 1
        F = []
        for i in range(n):
            f = (F0[i % (n // 2)] + x * F1[i % (n // 2)]) % p
            x = (x * w) % p
            F.append(f)
        return F

    def fft(self, A):
        return self.base(A, self.n, self.w)

    def ift(self, A):
        F = self.base(A, self.n, self.rw)
        return [(f * self.rn) % self.p for f in F]


if __name__ == "__main__":
    N = int(input())
    A, B = [0], [0]
    for i in range(1, N + 1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    n, p, w = 262144, 1541406721, 103
    fft = FFT(n, p, w)
    FA = fft.fft(A)
    FB = fft.fft(B)
    FC = [FA[i] * FB[i] for i in range(n)]
    C = fft.ift(FC)
    for k in range(1, 2 * N + 1):
        print(C[k])
