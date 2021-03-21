from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def unite(self, i, j):
        i, j = self.find(i), self.find(j)
        if i > j:
            i, j = j, i
        self.parent[j] = i


n, m = map(int, input().split())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    x, y = map(int, input().split())
    uf.unite(x - 1, y - 1)
sa, sb = defaultdict(int), defaultdict(int)
for i in range(n):
    sa[uf.find(i)] += a[i]
    sb[uf.find(i)] += b[i]
if all(sa[i] == sb[i] for i in sa):
    print("Yes")
else:
    print("No")
