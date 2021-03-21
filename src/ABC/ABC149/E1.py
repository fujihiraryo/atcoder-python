class FFT:
    def __init__(self, n, p, w):
        # pは素数で, wは1のn乗根(mod p)
        # 例:(n,p,w)=(4,5,2),(262144,347078657,13)
        self.n = n
        self.p = p
        self.w = w
        self.rn = pow(n, p - 2, p)
        self.rw = pow(w, p - 2, p)

    def base(self, A, n, w):
        if n == 1:
            return A
        p = self.p
        for i in range(n - len(A)):
            A.append(0)
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
        # 順変換
        return self.base(A, self.n, self.w)

    def ift(self, A):
        # 逆変換
        F = self.base(A, self.n, self.rw)
        return [(f * self.rn) % self.p for f in F]

    def conv(self, A, B):
        # AとBの畳み込み
        nA, nB = len(A), len(B)
        nC = nA + nB - 1
        FA = self.fft(A)
        FB = self.fft(B)
        FC = [(FA[i] * FB[i]) % self.p for i in range(self.n)]
        C = self.ift(FC)
        return C[:nC]


_, m = map(int, input().split())
(*A,) = map(int, input().split())
C = [0] * (max(A) + 1)
for a in A:
    C[a] += 1
CC = FFT(262144, 2662072321, 21).conv(C, C)
PC = []
for p, c in enumerate(CC):
    PC.append((p, c))
PC = PC[: 2 * max(A) + 1][::-1]
cnt = 0
power = 0
for p, c in PC:
    if cnt + c > m:
        break
    cnt += c
    power += p * c
power += (m - cnt) * p
print(power)
