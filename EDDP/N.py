n = int(input())
*A, = map(int, input().split())
S = [0]
for i in range(n):
    S.append(S[-1] + A[i])
DP = [[None for j in range(n + 1)] for i in range(n)]


def dp(i, j):
    if j <= i + 1:
        return 0
    if DP[i][j] is not None:
        return DP[i][j]
    DP[i][j] = S[j] - S[i] + min([dp(i, k) + dp(k, j)
                                  for k in range(i + 1, j)])
    return DP[i][j]


print(dp(0, n))
