class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        i, j = self.find(i), self.find(j)
        if i == j:
            return
        if i > j:
            i, j = j, i
        self.parent[j] = i
        self.count -= 1

    def same(self, i, j):
        return self.find(i) == self.find(j)


MOD = 998244353
n = int(input())
*f, = map(int, input().split())
uf = UnionFind(n)
for i in range(n):
    uf.unite(i, f[i] - 1)
print(pow(2, uf.count, MOD) - 1)
