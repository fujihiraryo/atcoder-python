n, k = map(int, input().split())
mod = 10**9+7
A = {}
ans = 0
for i in range(k, 0, -1):
    A[i] = pow(k//i, n, mod)
    for j in range(2*i, k+1, i):
        A[i] -= A[j]
    ans = (ans + A[i] * i) % mod
print(ans)
