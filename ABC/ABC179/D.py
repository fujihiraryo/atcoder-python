p = 998244353
n, k = map(int, input().split())
LRs = []
for j in range(k):
    lj, rj = map(int, input().split())
    LRs.append((lj, rj))
A = [0] * (n + 1)
i0 = min(lj for lj, rj in LRs)
A[0] = 1
A[i0] = 1
for i in range(i0 + 1, n):
    A[i] = A[i - 1]
    for j in range(k):
        lj, rj = LRs[j]
        if i - lj >= 0:
            A[i] += A[i - lj]
        if i - 1 - rj >= 0:
            A[i] -= A[i - 1 - rj]
        A[i] %= p
print(A[n - 1])
