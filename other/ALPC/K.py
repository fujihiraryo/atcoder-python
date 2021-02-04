MOD = 998244353
BIT = 30
MASK = (1 << BIT) - 1


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
            i0 >>= 1
            j0 >>= 1
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
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

    def range_merge(self, i, j):
        covering = [*self.__covering_index(i, j)]
        for k in covering[::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = self.fold(x, self.data[k])
        return x


def encode(x0, x1):
    return (x0 << BIT) + x1


def decode(x):
    return x >> BIT, x & MASK


def fold(x, y):
    x0, x1 = decode(x)
    y0, y1 = decode(y)
    z0 = (x0 + y0) % MOD
    z1 = x1 + y1
    return encode(z0, z1)


def compose(f, g):
    f0, f1 = decode(f)
    g0, g1 = decode(g)
    h0 = f0 * g0 % MOD
    h1 = (f0 * g1 + f1) % MOD
    return encode(h0, h1)


def apply(f, x):
    f0, f1 = decode(f)
    x0, x1 = decode(x)
    y0 = (f0 * x0 + f1 * x1) % MOD
    y1 = x1
    return encode(y0, y1)


def main():
    n, q = map(int, input().split())
    (*a,) = map(int, input().split())
    tree = LazySegmentTree(
        a=[encode(a[i], 1) for i in range(n)],
        ide=encode(0, 1),
        idf=encode(1, 0),
        fold=fold,
        compose=compose,
        apply=apply,
    )
    for _ in range(q):
        cmd, *query = map(int, input().split())
        if cmd == 0:
            i, j, b, c = query
            tree.range_apply(i, j, encode(b, c))
        else:
            i, j = query
            x, _ = decode(tree.range_merge(i, j))
            print(x)


if __name__ == "__main__":
    main()
