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


N, Q = map(int, input().split())
forest = UnionFind(N)
for q in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        forest.union(A, B)
    if P == 1:
        if forest.same(A, B):
            print("Yes")
        else:
            print("No")
