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


MOD = 998244353
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
row = UnionFind(n)
col = UnionFind(n)
for x in range(n - 1):
    for y in range(x + 1, n):
        if all(a[x][i] + a[y][i] <= k for i in range(n)):
            row.unite(x, y)
        if all(a[i][x] + a[i][y] <= k for i in range(n)):
            col.unite(x, y)
row_parents = set(row.find(x) for x in range(n))
col_parents = set(col.find(x) for x in range(n))
fct = [1] * (n + 1)
for i in range(n):
    fct[i + 1] = fct[i] * (i + 1) % MOD
row_prd = 1
for x in row_parents:
    row_prd *= fct[row.group_size[x]]
    row_prd %= MOD
col_prd = 1
for x in col_parents:
    col_prd *= fct[col.group_size[x]]
    col_prd %= MOD
print(row_prd * col_prd % MOD)
