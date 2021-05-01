from itertools import product


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


n, m = map(int, input().split())
edge = []
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    edge.append((a, b))
ans = 0
for s in product(range(2), repeat=n):
    if any(s[i] and s[j] for i, j in edge):
        continue
    uf = UnionFind(2 * n)
    for i, j in edge:
        if s[i] or s[j]:
            continue
        uf.unite(i, j + n)
        uf.unite(i + n, j)
    if any(uf.same(i, i + n) for i in range(n)):
        continue
    ans += 2 ** (uf.count // 2 - sum(s))
print(ans)
