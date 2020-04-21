import sys
input = sys.stdin.readline


class SegmentTree():
    # リストSの部分リストからなる集合を葉とするセグメント木
    def __init__(self, S, n):
        self.size = n
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
        # 配列のi番目をcに更新する
        tmp = i + 2**self.size - 1
        self.array[tmp] = {c}
        while tmp > 0:
            tmp = (tmp - 1) // 2
            self.array[tmp] = self.array[2 * tmp + 1] | self.array[2 * tmp + 2]


def main():
    n = int(input())
    S = list(input())
    S = [ord(s) for s in S]
    segtree = SegmentTree(S, 19)
    for _ in range(int(input())):
        t, i, c = input().split()
        if t == '1':
            segtree.update(int(i)-1, ord(c))
        if t == '2':
            print(segtree.query(int(i)-1, int(c)))


main()
