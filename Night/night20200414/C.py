import bisect
n, q = map(int, input().split())
S = list(input())
X = []
for i in range(n-1):
    if S[i] == 'A' and S[i+1] == 'C':
        X.append(i)
for j in range(q):
    l, r = map(int, input().split())
    a = bisect.bisect_left(X, l-1)
    b = bisect.bisect_left(X, r-1)
    print(b-a)
