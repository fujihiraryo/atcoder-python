import numpy as np

N, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
A = np.sort(np.array(A))
B = np.sort(np.array(B))
l, r = -10**18-1, 10**18+1
# 「積がxより小さいペアの数がK個未満」なるxの最大値を求める
while r - l > 1:
    c = (l+r)//2
    # a*b<cなる(a,b)の個数
    cnt = np.searchsorted(A, -(-c//B), side='left').sum()
    if cnt < K:
        l = c
    else:
        r = c
print(l)
