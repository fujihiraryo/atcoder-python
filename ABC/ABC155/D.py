import numpy as np


def count_pair(x):
    # A内のペアで積がxより小さいものの個数
    # まず(i,j)と(j,i)を重複して数える
    cnt = 0
    # A[i]<0なる各iに対してA[j]>x/A[i]なるjの個数
    cnt += (N - np.searchsorted(A, x // A_nega, side="right")).sum()
    if x > 0:
        # 各iに対してA[j]=0なるjの個数
        cnt += len(A_zero) * N
    # A[i]>0なる各iに対してA[j]<x/A[i]なるjの個数
    cnt += np.searchsorted(A, -(-x // A_posi), side="left").sum()
    # i=jを除いてから2で割る
    cnt = (cnt - (A ** 2 < x).sum()) // 2
    return cnt


# count_pair(x)<Kをみたすxの最大値を二分探索で求める
N, K = map(int, input().split())
(*A,) = map(int, input().split())
A = np.array(A)
A = np.sort(A)
A_posi = A[A > 0]
A_zero = A[A == 0]
A_nega = A[A < 0]
inf = 10 ** 18 + 1
l, r = -inf, inf
while r - l > 1:
    c = (l + r) // 2
    if count_pair(c) < K:
        l = c
    else:
        r = c
print(l)
