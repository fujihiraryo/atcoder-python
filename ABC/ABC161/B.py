n, m = map(int, input().split())
*A, = map(int, input().split())
A.sort(reverse=True)
if A[m-1] * 4 * m >= sum(A):
    print('Yes')
else:
    print('No')
