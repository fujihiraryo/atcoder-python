class Comb0():
    # あらかじめO(k)の前計算をしておいてr<=kに対してnCrを高速に計算する
    def __init__(self, n, k=10**6, p=10**9+7):
        # num[i]=nPi
        # den[i]=(i!)^(-1)
        num, den = [1], [1]
        a, b = 1, 1
        for i in range(1, k+1):
            a = (a*(n-i+1)) % p
            b = (b*pow(i, p-2, p)) % p
            num.append(a)
            den.append(b)
        self.num = num
        self.den = den
        self.n = n
        self.p = p

    def calc(self, r):
        num, den = self.num, self.den
        if r < 0 or self.n < r:
            return 0
        return (num[r] * den[r]) % self.p


n, a, b = map(int, input().split())
p = 10**9+7
cmb = Comb0(n, k=max(a, b))
print((pow(2, n, p)-1-cmb.calc(a)-cmb.calc(b)) % p)
