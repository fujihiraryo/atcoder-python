import sys
input = sys.stdin.readline


class SegmentTree():
    def __init__(self, S):
        self.size = 19
        self.array = [set()] * (2**(self.size + 1) - 1)
        for i, c in enumerate(S):
            self.array[i + 2**self.size - 1] = {c}
        for i in range(2**self.size - 1)[::-1]:
            self.array[i] = self.array[2 * i + 1] | self.array[2 * i + 2]

    def subquery(self, l, r, k, i, j):
        # 区間[i,j)の中で区間[l,r)の文字列の集合を返す
        if j <= l or r <= i:
            return set()
        elif l <= i and j <= r:
            return self.array[k]
        else:
            l_set = self.subquery(l, r, 2 * k + 1, i, (i + j) // 2)
            r_set = self.subquery(l, r, 2 * k + 2, (i + j) // 2, j)
            return l_set | r_set

    def query(self, l, r):
        # [l,r)に含まれる文字の種類数
        return len(self.subquery(l, r, 0, 0, 2**self.size))

    def update(self, i, c):
        tmp = i + 2**self.size - 1
        self.array[tmp] = {c}
        while tmp > 0:
            tmp = (tmp - 1) // 2
            self.array[tmp] = self.array[2 * tmp + 1] | self.array[2 * tmp + 2]


N = int(input())
S = [ord(_) - 97 for _ in list(input())]
Q = int(input())
tree = SegmentTree(S)
for q in range(Q):
    t, i, c = input().split()
    if t == '1':
        i = int(i) - 1
        tree.update(i, ord(c) - 97)
    else:
        l, r = int(i) - 1, int(c)
        print(tree.query(l, r))
