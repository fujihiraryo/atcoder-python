import sys
import random

input = sys.stdin.readline


class BIT:
    def __init__(self, n):
        self.size = n
        self.array = [0] * (n + 1)
        self.e = [0] * n

    def sum(self, i):
        s = 0
        tmp = i
        while tmp > 0:
            s += self.array[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        self.e[i] += x
        tmp = i + 1
        while tmp <= self.size:
            self.array[tmp] += x
            tmp += tmp & -tmp


def main():
    n, q = 5 * 10 ** 5, 5 * 10 ** 5
    C = [random.choice(range(1, n + 1)) for i in range(n)]
    P = [0] * n
    N = [0] * n
    for i in range(n)[::-1]:
        if P[C[i]]:
            N[i] = P[C[i]]
        P[C[i]] = i
    F = [0] * n
    B = BIT(n)
    for i in range(n):
        if F[C[i]] == 0:
            B.add(i, 1)
            F[C[i]] = 1
    # XY = sorted([(tuple(map(int, input().split())), j) for j in range(q)])
    XY = []
    for j in range(q):
        x = random.choice(range(1, n + 1))
        y = random.choice(range(x, n + 1))
        XY.append(((x, y), j))
    XY.sort()
    a = 0
    lst = [0] * q
    for (x, y), j in XY:
        for i in range(a, x - 1):
            B.add(N[i], 1)
        a = x - 1
        lst[j] = B.sum(y) - B.sum(x - 1)
    print(*lst, sep="\n")


main()
