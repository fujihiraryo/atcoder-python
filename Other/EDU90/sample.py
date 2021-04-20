class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, i):
        if self.parent[i] == -1:
            return i
        return self.find(self.parent[i])

    def same(self, i, j):
        return self.find(i) == self.find(j)

    def unite(self, i, j):
        i, j = self.find(i), self.find(j)
        if i == j:
            return
        self.parent[i] = j


uf = UnionFind(10)
uf.unite(0, 2)
uf.unite(2, 5)
print(uf.same(0, 5))
print(uf.same(0, 5))
