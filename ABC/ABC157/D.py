class UnionFind:
    def __init__(self, n):
        self.n = n
        # 親の名(いない場合は自分)
        self.parent = list(range(n))
        # 子の数
        self.count = [0] * n

    def root(self, x):
        # xの根を返す
        if self.parent[x] == x:
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


N, M, K = map(int, input().split())
tree = UnionFind(N)
# 同じグループでの友達の数とブロックの数
F, B = [0] * N, [0] * N
lst = []
for m in range(M):
    a, b = map(int, input().split())
    tree.union(a - 1, b - 1)
    lst.append((a, b))
for a, b in lst:
    if tree.same(a - 1, b - 1):
        F[a - 1] += 1
        F[b - 1] += 1
for k in range(K):
    c, d = map(int, input().split())
    if tree.same(c - 1, d - 1):
        B[c - 1] += 1
        B[d - 1] += 1
# nが属する木の大きさから友達の数とブロックの数と自分を除いたのが答え
print(*[tree.size(n) - F[n] - B[n] - 1 for n in range(N)])
