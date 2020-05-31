n, s = map(int, input().split())
*A, = map(int, input().split())
p = 998244353
DP = [[0 for j in range(s + 1)] for i in range(n + 1)]
DP[0][0] = 1
for i in range(n):
    for j in range(s + 1):
        if j >= A[i]:
            DP[i + 1][j] = (2 * DP[i][j] + DP[i][j - A[i]]) % p
        else:
            DP[i + 1][j] = (2 * DP[i][j]) % p
print(DP[n][s] % p)
