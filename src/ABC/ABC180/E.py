n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]
C = [[0] * n for _ in range(n)]
for i in range(n):
    xi, yi, zi = P[i]
    for j in range(n):
        xj, yj, zj = P[j]
        C[i][j] = abs(xi - xj) + abs(yi - yj) + max(0, zj - zi)
DP = [[1 << 30] * n for _ in range(1 << n)]
DP[0][0] = 0
for s in range(1 << n):
    for i in range(n):
        if (1 << i) & s:
            for j in range(n):
                DP[s][i] = min(DP[s][i], DP[s - (1 << i)][j] + C[j][i])
print(DP[(1 << n) - 1][0])
