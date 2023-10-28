class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.size = n

    def __find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.__find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        i, j = self.__find(i), self.__find(j)
        if i == j:
            return
        if i > j:
            i, j = j, i
        self.parent[j] = i
        self.size -= 1


h, w = map(int, input().split())


def num(i, j):
    return i * w + j


s = [input() for _ in range(h)]
cnt = 0
uf = UnionFind(h * w)
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            cnt += 1
            continue
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if 0 <= i + di < h and 0 <= j + dj < w and s[i + di][j + dj] == "#":
                    uf.unite(num(i, j), num(i + di, j + dj))
print(uf.size - cnt)
