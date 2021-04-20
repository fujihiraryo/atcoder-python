class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def root(self, i):
        if self.parent[i] == -1:
            return i
        self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def same(self, i, j):
        return self.root(i) == self.root(j)

    def merge(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j:
            return
        self.parent[j] = i


h, w = map(int, input().split())
q = int(input())
red = [[0] * w for _ in range(h)]
uf = UnionFind(h * w)
for _ in range(q):
    t, *query = map(lambda x: int(x) - 1, input().split())
    if t == 0:
        r, c = query
        red[r][c] = 1
        if r - 1 >= 0 and red[r - 1][c]:
            uf.merge((r - 1) * h + c, r * h + c)
        if r + 1 < h and red[r + 1][c]:
            uf.merge(r * h + c, (r + 1) * h + c)
        if c - 1 >= 0 and red[r][c - 1]:
            uf.merge(r * h + c - 1, r * h + c)
        if c + 1 < w and red[r][c + 1]:
            uf.merge(r * h + c, r * h + c + 1)
    else:
        ra, ca, rb, cb = query
        if red[ra][ca] and red[rb][cb] and uf.same(ra * h + ca, rb * h + cb):
            print("Yes")
        else:
            print("No")
