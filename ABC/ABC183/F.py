from collections import defaultdict


class UnionFind:
    def __init__(self, n, C):
        # 親の名
        self.parent = [i for i in range(n)]
        # 子のクラス管理
        self.dic = [defaultdict(lambda: 0) for i in range(n)]
        for i in range(n):
            self.dic[i][C[i]] = 1

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
        for key in self.dic[y0].keys():
            self.dic[x0][key] += self.dic[y0][key]


n, q = map(int, input().split())
(*C,) = map(lambda x: int(x) - 1, input().split())
uf = UnionFind(n, C)
for _ in range(q):
    t, a, b = map(lambda x: int(x) - 1, input().split())
    if t == 0:
        uf.union(a, b)
    else:
        print(uf.dic[uf.root(a)][b])
