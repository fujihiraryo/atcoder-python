m, n = map(int, input().split())
(*A,) = map(int, input().split())
(*B,) = map(int, input().split())
INF = 10 ** 20
DP = [[INF] * (n + 1) for _ in range(m + 1)]
for i in range(m + 1):
    DP[i][0] = i
for j in range(n + 1):
    DP[0][j] = j
for i in range(m):
    for j in range(n):
        if A[i] == B[j]:
            DP[i + 1][j + 1] = DP[i][j]
        else:
            DP[i + 1][j + 1] = min(DP[i][j], DP[i + 1][j], DP[i][j + 1]) + 1
print(DP[m][n])
