import sys

input = sys.stdin.readline


class LazySegmentTree:
    def __init__(self, n, ide, ope, init=None):
        self.size = 1 << (n - 1).bit_length()
        self.data = [ide] * (self.size << 1)
        if init is not None:
            for i in range(n):
                self.data[i + self.size] = init[i]
        for k in range(1, self.size)[::-1]:
            self.data[k] = self.data[2 * k] + self.data[2 * k + 1]
        self.memo = [ope] * (self.size << 1)
        self.ide = ide
        self.ope = ope

    def __covering_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        i1 = (i0 // (i0 & -i0)) >> 1
        j1 = (j0 // (j0 & -j0)) >> 1
        while i0 < j0:
            if j0 <= j1:
                yield j0
            if i0 <= i1:
                yield i0
            i0 >>= 1
            j0 >>= 1
        while i0:
            yield i0
            i0 >>= 1

    def __covered_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
                yield i0
                i0 += 1
            if j0 & 1:
                yield j0 - 1
            i0 >>= 1
            j0 >>= 1
        # i0 = i + self.size
        # j0 = j + self.size
        # while i0 < j0:
        #     if i0 & 1:
        #         i0 += 1
        #     if j0 & 1:
        #         yield j0 - 1
        #     i0 >>= 1
        #     j0 >>= 1

    def __lazy_update(self, k):
        if self.memo[k] == self.ope:
            return
        if k < self.size:
            self.memo[k << 1] = self.memo[k] * self.memo[k << 1]
            self.data[k << 1] = self.memo[k](self.data[k << 1])
            self.memo[k << 1 | 1] = self.memo[k] * self.memo[k << 1 | 1]
            self.data[k << 1 | 1] = self.memo[k](self.data[k << 1 | 1])
        self.memo[k].__init__()

    def range_update(self, i, j, ope):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        for k in self.__covered_index(i, j):
            self.memo[k] = ope * self.memo[k]
            self.data[k] = ope(self.data[k])
        for k in self.__covering_index(i, j):
            left = self.data[k << 1]
            right = self.data[k << 1 | 1]
            self.data[k] = left + right

    def range_merge(self, i, j):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = x + self.data[k]
        return x


class Monoid:
    # example(Range Sum)
    def __init__(self, value=0, length=1, MOD=998244353):
        self.value = value
        self.length = length
        self.MOD = MOD

    def __add__(self, other):
        value = self.value + other.value
        length = self.length + other.length
        return Monoid(value % self.MOD, length)


class Operator:
    # example(Range Affine)
    def __init__(self, param=(1, 0), MOD=998244353):
        self.param = param
        self.MOD = MOD

    def __call__(self, monoid):
        b, c = self.param
        value = b * monoid.value + monoid.length * c
        return Monoid(value % self.MOD, monoid.length)

    def __mul__(self, other):
        b0, c0 = self.param
        b1, c1 = other.param
        b, c = b0 * b1, b0 * c1 + c0
        return Operator((b % self.MOD, c % self.MOD))

    def __eq__(self, other):
        return self.param == other.param


n, q = map(int, input().split())
(*a,) = map(int, input().split())
a = [Monoid(a[i], 1) for i in range(n)]
tree = LazySegmentTree(n, Monoid(), Operator(), init=a)
ans = []
for _ in range(q):
    cmd, *query = map(int, input().split())
    if cmd == 0:
        i, j, b, c = query
        tree.range_update(i, j, Operator((b, c)))
    else:
        i, j = query
        ans.append(tree.range_merge(i, j).value)
print(*ans, sep="\n")
