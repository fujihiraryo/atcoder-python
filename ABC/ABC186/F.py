class SegmentTree:
    def __init__(self, size):
        self.size = 1 << size.bit_length()
        self.tree = [0] * (self.size << 1)

    def __getitem__(self, i):
        return self.tree[i + self.size]

    def update(self, i, x):
        i0 = i + self.size
        x0 = x
        while i0:
            self.tree[i0] = x0
            x0 = self.tree[i0] + self.tree[i0 ^ 1]
            i0 >>= 1

    def range(self, i, j):
        x = 0
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
                x += self.tree[i0]
                i0 += 1
            if j0 & 1:
                x += self.tree[j0 - 1]
            i0 >>= 1
            j0 >>= 1
        return x


h, w, m = map(int, input().split())
row, col = [w] * h, [h] * w
obs = [[] for _ in range(h)]
for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())
    row[i] = min(row[i], j)
    col[j] = min(col[j], i)
    obs[i].append(j)
ans = sum(row[: col[0]]) + sum(col[: row[0]])
tree = SegmentTree(w)
for j in range(w):
    tree.update(j, 1)
for i in range(col[0]):
    for j in obs[i]:
        tree.update(j, 0)
    ans -= tree.range(0, min(row[0], row[i]))
print(ans)
