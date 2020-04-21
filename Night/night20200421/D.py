class UnionFind():
    def __init__(self, n):
        self.n = n
        # 親の名(いない場合はNone)
        self.parent = [None]*n
        # 子の数
        self.count = [0] * n

    def root(self, x):
        # xの根を返す
        if self.parent[x] == None:
            return x
        else:
            return self.root(self.parent[x])

    def union(self, x, y):
        # xとyをまとめる
        x0 = self.root(x)
        y0 = self.root(y)
        if x0 == y0:
            return
        if x0 > y0:
            x0, y0 = y0, x0
        self.parent[y0] = x0
        self.count[x0] += self.count[y0] + 1

    def size(self, x):
        # xの属する木の大きさ
        return self.count[self.root(x)] + 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


n, m, k = map(int, input().split())
uf = UnionFind(n)
# F[i]=iの友達の数
F = [0]*n
# B[i]=iと同じグループでブロックしている数
B = [0]*n
for i in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)
    F[a-1] += 1
    F[b-1] += 1
for j in range(k):
    a, b = map(int, input().split())
    if uf.same(a-1, b-1):
        B[a-1] += 1
        B[b-1] += 1
L = [uf.size(i)-1-F[i]-B[i] for i in range(n)]
print(*L)
