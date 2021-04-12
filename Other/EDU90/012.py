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


h, w = map(int, input().split())
num = lambda x, y: (x - 1) * h + y - 1
n = h * w
q = int(input())
uf = UnionFind(n)
red = [0] * n
for _ in range(q):
    t, *query = map(int, input().split())
    if t == 1:
        x, y = query
        i = num(x, y)
        red[i] = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < h and 0 <= y + dy < w:
                j = num(x + dx, y + dy)
                if red[j]:
                    uf.unite(i, j)
    else:
        xa, ya, xb, yb = query
        i, j = num(xa, ya), num(xb, yb)
        if uf.find(i) == uf.find(j) and red[i] and red[j]:
            print("Yes")
        else:
            print("No")
