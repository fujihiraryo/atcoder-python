h, n = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(n)]
A = [a for a, b in AB]
B = [b for a, b in AB]
inf = 10 ** 10
# DP[i][j]=i個以内で体力j以上削るための消費魔力の最小値
DP = [[inf for j in range(h + 1)] for i in range(n + 1)]
DP[0][0] = 0
for i in range(n):
    for j in range(h + 1):
        DP[i + 1][j] = min(DP[i][j], DP[i + 1][max(0, j - A[i])] + B[i])
print(DP[n][h])
