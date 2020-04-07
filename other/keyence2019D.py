import bisect
n, m = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
setA = set(A)
setB = set(B)
A.sort()
B.sort()
if len(setA) < n or len(setB) < m:
    print(0)
    exit()
mod = 10 ** 9 + 7
cnt = 1
for i in range(n * m, 0, -1):
    cntA = n-bisect.bisect_left(A, i)
    cntB = m-bisect.bisect_left(B, i)
    if i in setA and i not in setB:
        cnt = (cnt*cntB) % mod
    if i not in setA and i in setB:
        cnt = (cnt*cntA) % mod
    if i not in setA and i not in setB:
        cnt = (cnt*(cntA*cntB-(n*m-i))) % mod
print(cnt)
