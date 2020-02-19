import numpy as np


def count_pair(A, x):
    # A内のペアで積がxより小さいものの個数
    N = len(A)
    cnt = 0
    for n in range(N - 1):
        if A[n] < 0:
            y = x // A[n]
            # n+1番以降でyより大きいものの個数
            cnt += N-max(n+1, np.searchsorted(A, y, side='right'))
        elif A[n] > 0:
            y = -(-x // A[n])
            # n+1番以降でyより小さいものの個数
            cnt += max(n+1, np.searchsorted(A, y, side='left')) - (n + 1)
        else:  # A[n]==0
            if x > 0:
                cnt += N - n - 1
    return cnt


# count_pair(x)<Kをみたすxの最大値を求める
N, K = map(int, input().split())
* A, = map(int, input().split())
A.sort()
inf = 10**18+1
l, r = -inf, inf
while r - l > 1:
    c = (l + r) // 2
    if count_pair(A, c) < K:
        l = c
    else:
        r = c
print(l)
