n = int(input())
mod = 10 ** 9 + 7
C = [[0 for j in range(n + 1)] for i in range(n + 1)]
for i in range(n + 1):
    C[i][0] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod
ans = 0
k = 1
while 3 * k <= n:
    ans += C[n - 2 * k - 1][k - 1]
    ans %= mod
    k += 1
print(ans)
