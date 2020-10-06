n, m = map(int, input().split())
WV = [tuple(map(int, input().split())) for i in range(n)]
W = [w for w, v in WV]
V = [v for w, v in WV]
inf = 10 ** 10
sumV = sum(V)
DP = [[inf for j in range(sumV + 1)] for i in range(n + 1)]
DP[0][0] = 0
for i in range(1, n + 1):
    for j in range(V[i - 1]):
        DP[i][j] = DP[i - 1][j]
    for j in range(V[i - 1], sumV + 1):
        DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - V[i - 1]] + W[i - 1])
for j in range(sumV, 0, -1):
    if DP[n][j] <= m:
        print(j)
        exit()
