from itertools import combinations


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
        return j

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parent[j0] = i0


MOD = 998244353
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
fct = [1]
for i in range(1, n ** 2 + 1):
    fct.append(fct[-1] * i % MOD)
raw_uf = UnionFind(n)
col_uf = UnionFind(n)
for i, j in combinations(range(n), 2):
    if all(a[i][x] + a[j][x] <= k for x in range(n)):
        raw_uf.unite(i, j)
    if all(a[x][i] + a[x][j] <= k for x in range(n)):
        col_uf.unite(i, j)
raw_count = [0] * n
col_count = [0] * n
for i in range(n):
    raw_count[raw_uf.find(i)] += 1
    col_count[col_uf.find(i)] += 1
ans = 1
for i in range(n):
    ans = ans * fct[raw_count[i]] * fct[col_count[i]] % MOD
print(ans)
