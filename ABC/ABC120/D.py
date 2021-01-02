class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.count = [1] * size

    def find(self, i):
        i0 = i
        while self.parent[i0] != i0:
            i0 = self.parent[i0]
        return i0

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        if i0 != j0:
            self.count[i0] += self.count[j0]
        self.parent[j0] = i0

    def group_size(self, i):
        i0 = self.find(i)
        return self.count[i0]


n, m = map(int, input().split())
edge = [map(int, input().split()) for _ in range(m)]
edge.reverse()
ans = [n * (n - 1) // 2]
uf = UnionFind(n)
for x, y in edge[:-1]:
    tmp = ans[-1]
    if uf.find(x - 1) != uf.find(y - 1):
        a = uf.group_size(x - 1)
        b = uf.group_size(y - 1)
        tmp += a * (a - 1) // 2 + b * (b - 1) // 2
        uf.unite(x - 1, y - 1)
        c = uf.group_size(x - 1)
        tmp -= c * (c - 1) // 2
    ans.append(tmp)
print(*ans[::-1], sep="\n")
