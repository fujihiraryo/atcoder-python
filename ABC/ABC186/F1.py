class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * (n + 1)

    def __getitem__(self, i):
        return self.sum(i + 1) - self.sum(i)

    def sum(self, i):
        s = 0
        tmp = i
        while tmp:
            s += self.arr[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        tmp = i + 1
        while tmp <= self.size:
            self.arr[tmp] += x
            tmp += tmp & -tmp


h, w, m = map(int, input().split())
row, col = [w] * h, [h] * w
obs = [[] for _ in range(h)]
for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())
    row[i] = min(row[i], j)
    col[j] = min(col[j], i)
    obs[i].append(j)
ans = sum(row[: col[0]]) + sum(col[: row[0]])
tree = FenwickTree(w)
for j in range(row[0]):
    tree.add(j, 1)
for i in range(col[0]):
    for j in obs[i]:
        tree.add(j, -tree[j])
    ans -= tree.sum(row[i])
print(ans)
