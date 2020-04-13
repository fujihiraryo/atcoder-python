import bisect
n = int(input())
A = [int(input()) for i in range(n)]
m = 10**9
X = []
for a in A:
    i = bisect.bisect_right(X, -a)
    if i == len(X):
        X.append(-a)
    else:
        X[i] = -a
print(len(X))
