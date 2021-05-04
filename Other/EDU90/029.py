class LazySegmentTree:
    def __init__(self, a, ide, idf, fold, compose, apply):
        self.size = len(a)
        self.ide = ide
        self.idf = idf
        self.fold = fold
        self.compose = compose
        self.apply = apply
        self.data = [self.ide] * (self.size << 1)
        self.memo = [self.idf] * (self.size << 1)
        self.data[self.size :] = a
        for k in range(1, self.size)[::-1]:
            self.data[k] = self.fold(self.data[k << 1], self.data[k << 1 | 1])

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

    def __lazy_update(self, k):
        if self.memo[k] == self.idf:
            return
        if k < self.size:
            self.memo[k << 1] = self.compose(self.memo[k], self.memo[k << 1])
            self.data[k << 1] = self.apply(self.memo[k], self.data[k << 1])
            self.memo[k << 1 | 1] = self.compose(self.memo[k], self.memo[k << 1 | 1])
            self.data[k << 1 | 1] = self.apply(self.memo[k], self.data[k << 1 | 1])
        self.memo[k] = self.idf

    def range_apply(self, i, j, f):
        covering = [*self.__covering_index(i, j)]
        for k in covering[::-1]:
            self.__lazy_update(k)
        for k in self.__covered_index(i, j):
            self.memo[k] = self.compose(f, self.memo[k])
            self.data[k] = self.apply(f, self.data[k])
        for k in covering:
            self.data[k] = self.fold(self.data[k << 1], self.data[k << 1 | 1])

    def range_fold(self, i, j):
        covering = [*self.__covering_index(i, j)]
        for k in covering[::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = self.fold(x, self.data[k])
        return x


w, n = map(int, input().split())
a = LazySegmentTree([0] * w, 0, lambda x: x, max, lambda f, g: f, lambda f, x: f)
for _ in range(n):
    l, r = map(int, input().split())
    x = a.range_fold(l - 1, r) + 1
    print(x)
    a.range_apply(l - 1, r, x)
