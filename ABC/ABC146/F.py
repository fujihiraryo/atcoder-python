INF = 1 << 30


class SegmentTree:
    def __init__(self, size):
        self.size = 1 << size.bit_length()
        self.tree = [(INF, -1)] * (self.size << 1)

    def __getitem__(self, i):
        return self.tree[i + self.size]

    def update(self, i, x):
        i0 = i + self.size
        while i0:
            self.tree[i0] = x
            x = min(self.tree[i0], self.tree[i0 ^ 1])
            i0 >>= 1

    def range(self, i, j):
        x = (INF, -1)
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
                x = min(x, self.tree[i0])
                i0 += 1
            if j0 & 1:
                x = min(x, self.tree[j0 - 1])
            i0 >>= 1
            j0 >>= 1
        return x


n, m = map(int, input().split())
s = input()
tree = SegmentTree(n + 1)
tree.update(0, (0, 0))
back = [-1] * (n + 1)
for i in range(1, n + 1):
    if s[i] == "1":
        tree.update(i, (INF, i))
        continue
    x, j = tree.range(max(0, i - m), i)
    tree.update(i, (x + 1, i))
    back[i] = j
if back[n] == -1:
    print(-1)
    exit()
ans = []
tmp = n
while back[tmp] != -1:
    ans.append(tmp - back[tmp])
    tmp = back[tmp]
print(*ans[::-1])
