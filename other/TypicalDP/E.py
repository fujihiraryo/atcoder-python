d = int(input())
n = int(input())
p = 10**9+7
N = [int(i) for i in list(str(n))]
X = [sum([1 for k in range(N[0]) if k % d == j]) for j in range(d)]
Y = [sum([1 for k in range(N[0]+1) if k % d == j]) for j in range(d)]
for i in range(1, len(N)):
    r = N[i]-1
    X_ = [0]*d
    for j in range(d):
        x = 0
        for k in range(r+1):
            x += Y[(j-k) % d]
        for k in range(r+1, 10):
            x += X[(j-k) % d]
        X_[j] = x % p
    r += 1
    Y_ = [0]*d
    for j in range(d):
        y = 0
        for k in range(r+1):
            y += Y[(j-k) % d]
        for k in range(r+1, 10):
            y += X[(j-k) % d]
        Y_[j] = y % p
    X, Y = X_, Y_
print(Y[0]-1)
