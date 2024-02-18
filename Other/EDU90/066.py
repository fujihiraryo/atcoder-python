class BIT:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * (n + 1)

    def __getitem__(self, i):
        return self.sum(i + 1) - self.sum(i)

    def sum(self, i):
        s = 0
        tmp = i
        while tmp:
            s += self.arr[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        tmp = i + 1
        while tmp <= self.size:
            self.arr[tmp] += x
            tmp += tmp & -tmp


def inversion(a):
    size = max(a)
    b = BIT(size + 1)
    res = 0
    for i in range(len(a)):
        res += b.sum(size + 1) - b.sum(a[i])
        b.add(a[i], 1)
    return res


n = int(input())
MAX = 101
b = BIT(MAX)
ans = 0
for _ in range(n):
    l, r = map(int, input().split())
    for x in range(l, r + 1):
        ans += (b.sum(MAX) - b.sum(x + 1)) / (r - l + 1)
        b.add(x, 1 / (r - l + 1))
print(ans)
