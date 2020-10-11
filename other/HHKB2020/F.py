class Mint:
    def __init__(self, val, MOD=10 ** 9 + 7):
        self.val = val % MOD
        self.MOD = MOD

    def __repr__(self):
        return str(self.val)

    def __add__(self, other):
        return Mint((self.val + other.val) % self.MOD)

    def __sub__(self, other):
        return Mint((self.val - other.val) % self.MOD)

    def __mul__(self, other):
        return Mint((self.val * other.val) % self.MOD)

    def __truediv__(self, other):
        return self.__mul__(other.__inv__())

    def __pow__(self, p):
        return Mint(pow(self.val, p, self.MOD))

    def __inv__(self):
        return Mint(pow(self.val, self.MOD - 2, self.MOD))


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __mul__(self, other):
        m = len(self.coefficients)
        n = len(other.coefficients)
        coefficients = [Mint(0)] * (m + n - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                coefficients[i + j] = coefficients[i + j] + a * b
        return Polynomial(coefficients)

    def substitute(self, x):
        y = Mint(0)
        for i, a in enumerate(self.coefficients):
            y = y + a * x ** i
        return y

    def antiderivative(self):
        coefficients = [Mint(0)] * (len(self.coefficients) + 1)
        for i, a in enumerate(self.coefficients):
            coefficients[i + 1] = a / Mint(i + 1)
        return Polynomial(coefficients)

    def integrate(self, a, b):
        P = self.antiderivative()
        return P.substitute(b) - P.substitute(a)


INF = 10 ** 9
n = int(input())
L, R = [], []
for i in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
maxL = max(L)
IDs = [i for i in range(n) if maxL < R[i]]
IDs.sort(key=lambda i: R[i], reverse=True)
L = [Mint(l) for l in L]
R = [Mint(r) for r in R]
ans = Mint(INF)
b = Mint(INF)
poly = Polynomial([Mint(1)])
for i in IDs:
    a = R[i]
    ans = ans - poly.integrate(a, b)
    poly = poly * Polynomial([Mint(-1) * L[i] / (R[i] - L[i]), Mint(1) / (R[i] - L[i])])
    b = a
a = Mint(maxL)
ans = ans - poly.integrate(a, b)
for i in range(n):
    ans = ans * Mint(i + 2) * (R[i] - L[i])
print(ans)
