import math
n, q = map(int, input().split())
*A, = map(int, input().split())
*S, = map(int, input().split())
a = A[0]
B = [a]
for i in range(1, n):
    a = math.gcd(a, A[i])
    B.append(a)
for s in S:
    l, r = -1, n
    while r-l > 1:
        c = (l+r)//2
        if math.gcd(s, B[c]) == 1:
            r = c
        else:
            l = c
    if r == n:
        print(math.gcd(s, B[n-1]))
    else:
        print(r+1)
