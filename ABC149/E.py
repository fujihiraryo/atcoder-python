import numpy as np

N, M = map(int, input().split())
*A, = map(int, input().split())
A = np.sort(np.array(A))
l, r = 0, 2*(10**5)+1
while r-l > 1:
    c = (l+r)//2
    # A[i]+A[j]<cとなる(i,j)の個数
    K = np.searchsorted(A, c-A, side='left').sum()
    if K < N**2 - M:
        l = c
    else:
        r = c
# 和がr以上のペアの和の合計を求める
ans = 0
j = 0
# S:Aの累積和
S = np.cumsum(A)
I = np.searchsorted(A, r-A, side='left')
print(r)
print(A)
print(S)
print(I)
for i in range(N):
    ans += (N-I[i])*A[i]
    if I[i] == 0:
        ans += S[N-1]
    elif I[i] < N:
        ans += S[N-1]-S[I[i]-1]
print(ans)
