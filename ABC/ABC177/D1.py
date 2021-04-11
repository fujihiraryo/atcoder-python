class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.group_size = [1] * n

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
            self.parent[i] = j
        return j

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parent[j0] = i0
        if i0 != j0:
            self.group_size[i0] += self.group_size[j0]


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.unite(a - 1, b - 1)
print(max(uf.group_size[i] for i in range(n)))
