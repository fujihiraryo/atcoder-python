class SegmentTree:
    def __init__(self, size):
        self.size = 1 << (size - 1).bit_length()
        self.tree = [0] * (self.size << 1)

    def get(self, i):
        return self.tree[i + self.size]

    def update(self, i, x):
        i += self.size
        while i > 0:
            self.tree[i] = x
            x = self.tree[i] ^ self.tree[i ^ 1]
            i >>= 1

    def query(self, i, j):
        x = 0
        i += self.size
        j += self.size
        while i < j:
            if i & 1:
                x ^= self.tree[i]
                i += 1
            if j & 1:
                x ^= self.tree[j - 1]
            i >>= 1
            j >>= 1
        return x


n, q = map(int, input().split())
(*A,) = map(int, input().split())
query = [map(int, input().split()) for _ in range(q)]
tree = SegmentTree(n)
for i, a in enumerate(A):
    tree.update(i, a)
for t, x, y in query:
    if t == 1:
        a = tree.get(x - 1)
        tree.update(x - 1, a ^ y)
    else:
        print(tree.query(x - 1, y))
