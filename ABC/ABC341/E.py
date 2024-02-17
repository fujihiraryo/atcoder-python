class SegmentTree:
    def __init__(self, a):
        self.size = len(a)
        self.data = [0] * self.size * 2
        self.data[self.size :] = a
        for k in range(1, self.size)[::-1]:
            self.data[k] = self.data[2 * k] + self.data[2 * k + 1]

    def __covered_index(self, i, j):
        i += self.size
        j += self.size
        while i < j:
            if i % 2 == 1:
                yield i
                i += 1
            if j % 2 == 1:
                yield j - 1
            i //= 2
            j //= 2

    def update(self, i):
        i += self.size
        self.data[i] ^= 1
        while i:
            i //= 2
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]

    def sum(self, i, j):
        x = 0
        for k in self.__covered_index(i, j):
            x += self.data[k]
        return x


n, q = map(int, input().split())
s = input()
a = [1] + [int(s[i] != s[i + 1]) for i in range(n - 1)] + [1]
seg = SegmentTree(a)
for _ in range(q):
    t, i, j = map(int, input().split())
    if t == 1:
        seg.update(i - 1)
        seg.update(j)
    else:
        if seg.sum(i, j) == j - i:
            print("Yes")
        else:
            print("No")
