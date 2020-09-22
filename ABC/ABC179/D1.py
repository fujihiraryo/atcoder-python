p = 998244353
n, k = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(k)]
A = [0] * (2 * n + 1)
for l, r in LR:
    A[l] += 1
    A[r + 1] -= 1
s = 0
for i in range(1, n):
    s = (s + A[i]) % p
    for l, r in LR:
        A[i + l] += s
        A[i + r + 1] -= s
print(s)
