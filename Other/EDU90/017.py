class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.a[i] += x
            i += i & -i


n, m = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(m)]
lst.sort()
l = [lr[0] for lr in lst]
r = [lr[1] for lr in lst]
ans = 0
cur = 0
bit = BIT(n)
for j in range(m):
    if l[j] != l[cur]:
        for i in range(cur, j):
            bit.add(r[i], 1)
        cur = j
    ans += bit.sum(r[j]) - bit.sum(l[j] + 1)
print(ans)
