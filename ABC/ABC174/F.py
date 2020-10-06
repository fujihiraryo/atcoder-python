import sys

input = sys.stdin.readline


class BIT:
    def __init__(self, n):
        self.array = [0] * (n + 1)
        self.size = n

    def sum(self, i):
        s = 0
        tmp = i
        while tmp > 0:
            s += self.array[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        tmp = i + 1
        while tmp <= self.size:
            self.array[tmp] += x
            tmp += tmp & -tmp


n, q = map(int, input().split())
(*C,) = map(lambda x: int(x) - 1, input().split())
P = [0] * n
N = [None] * n
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
XY = [tuple(map(int, input().split())) for j in range(q)]
ids = list(range(q))
ids.sort(key=lambda j: XY[j][0])
a = 0
lst = [0] * q
for j in ids:
    x, y = XY[j]
    for i in range(a, x - 1):
        if N[i]:
            B.add(N[i], 1)
    a = x - 1
    lst[j] = B.sum(y) - B.sum(x - 1)
print(*lst, sep="\n")
