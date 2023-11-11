from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.n = n

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

    def connected(self):
        for i in range(n):
            self.find(i)
        parent = sorted(self.parent)
        return parent[0] == parent[-1]


n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

ans = k
for es in combinations(edges, n - 1):
    uf = UnionFind(n)
    score = 0
    for x, y, w in es:
        uf.unite(x, y)
        score = (score + w) % k
    if uf.connected():
        ans = min(ans, score)
print(ans)
