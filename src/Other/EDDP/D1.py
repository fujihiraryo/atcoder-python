n, m = map(int, input().split())
WV = [tuple(map(int, input().split())) for i in range(n)]
W = [w for w, v in WV]
V = [v for w, v in WV]
DP = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(W[i - 1]):
        DP[i][j] = DP[i - 1][j]
    for j in range(W[i - 1], m + 1):
        DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - W[i - 1]] + V[i - 1])
print(DP[n][m])
