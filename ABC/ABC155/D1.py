import numpy as np


def count_pair(x):
    cnt = 0
    cnt += (n - np.searchsorted(A, x // A_nega, side="right")).sum()
    if x > 0:
        cnt += len(A_zero) * n
    cnt += np.searchsorted(A, -(-x // A_posi), side="left").sum()
    cnt = (cnt - (A ** 2 < x).sum()) // 2
    return cnt


n, k = map(int, input().split())
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
    if count_pair(c) < k:
        l = c
    else:
        r = c
print(l)
