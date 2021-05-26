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


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort()
uf = UnionFind(n + 1)
ans = 0
for c, l, r in edges:
    if uf.find(l - 1) == uf.find(r):
        continue
    uf.unite(l - 1, r)
    ans += c
print(ans if uf.count == 1 else -1)
