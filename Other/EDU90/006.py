class SparseTable:
    def __init__(self, a):
        self.a = a
        n = len(a)
        table = [[i] for i in range(n)]
        for k in range(n.bit_length()):
            for i in range(n):
                if i + 2 ** (k + 1) > n:
                    continue
                x = table[i][k]
                y = table[i + 2 ** k][k]
                table[i].append(min(x, y, key=lambda i: a[i]))
        self.table = table
        self.bit_length = [i.bit_length() for i in range(n + 1)]

    def range(self, i, j):
        k = self.bit_length[j - i] - 1
        return min(self.table[i][k], self.table[j - 2 ** k][k], key=lambda i: self.a[i])


n, k = map(int, input().split())
s = input()
table = SparseTable(s)
l, r = 0, n - k + 1
ans = []
for _ in range(k):
    i = table.range(l, r)
    ans.append(s[i])
    l, r = i + 1, r + 1
print("".join(ans))
