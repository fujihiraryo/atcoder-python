n = int(input())
ABC = [tuple(map(int, input().split())) for i in range(n)]
A = [a for a, b, c in ABC]
B = [b for a, b, c in ABC]
C = [c for a, b, c in ABC]
DP = [[0 for j in range(3)] for i in range(n + 1)]
for i in range(1, n + 1):
    DP[i][0] = max(DP[i - 1][1], DP[i - 1][2]) + A[i - 1]
    DP[i][1] = max(DP[i - 1][2], DP[i - 1][0]) + B[i - 1]
    DP[i][2] = max(DP[i - 1][0], DP[i - 1][1]) + C[i - 1]
print(max(DP[n]))
