def f0(n, d):
    cnt = 0
    for i in range(1, n+1):
        if sum([int(_) for _ in list(str(i))]) % d == 0:
            cnt += 1
    return cnt


def f1(n, d):
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
    return Y[0]-1


for n in range(1, 1000):
    for d in range(1, 100+1):
        if f0(n, d) != f1(n, d):
            print(f0(n, d), f1(n, d))
