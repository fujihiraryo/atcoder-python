import copy
N, M = map(int, input().split())
W, V = [], []
for n in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
# f[m]=m以下の重さで最大の価値
f = [0 for m in range(M + 1)]
for n in range(N):
    f_ = copy.copy(f)
    for m in range(M + 1):
        if m >= W[n]:
            f_[m] = max(f[m], f[m - W[n]] + V[n])
    f = f_
print(f[M])
