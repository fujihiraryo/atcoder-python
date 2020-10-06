n, s = map(int, input().split())
(*A,) = map(int, input().split())
p = 998244353
DP = [[0 for j in range(s + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(s + 1):
        DP[i][j] += DP[i - 1][j]
        if j >= A[i - 1]:
            DP[i][j] += DP[i - 1][j - A[i - 1]]
        if j == A[i - 1] or j == 0:
            DP[i][j] += 1
        DP[i][j] %= p
ans = 0
for i in range(1, n + 1):
    ans += DP[i][s]
    ans %= p
print(ans)
