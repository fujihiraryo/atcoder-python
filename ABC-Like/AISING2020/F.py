mod = 10 ** 9 + 7
k = 5


class Lagrange:
    def __init__(self, lst):
        self.lst = lst

    def prd(self, j, x):
        tmp = 1
        for i, (xi, yi) in enumerate(self.lst):
            if j != i:
                tmp *= x - xi
                tmp %= mod
        return tmp

    def pln(self, x):
        tmp = 0
        for i, (xi, yi) in enumerate(self.lst):
            tmp += yi * (self.prd(i, x) * pow(self.prd(i, xi), mod - 2, mod))
            tmp %= mod
        return tmp


def cmb(x, y):
    if x < y:
        return 0
    tmp = 1
    for i in range(y):
        tmp *= x - i
        tmp *= pow(y - i, mod - 2, mod)
        tmp %= mod
    return tmp


def pln(n):
    tmp = 0
    for x in range(n):
        tmp += cmb(x + k - 1, k - 1) * cmb(n - (2 * x) + k, 2 * k)
        tmp %= mod
    return tmp


lst_eve = [(i, pln(i)) for i in range(0, 6 * k + 1, 2)]
lst_odd = [(i, pln(i)) for i in range(1, 6 * k + 2, 2)]

lag_eve = Lagrange(lst_eve)
lag_odd = Lagrange(lst_odd)

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(lag_eve.pln(n))
    else:
        print(lag_odd.pln(n))
