n = int(input())
(*A,) = map(int, input().split())
a, b, c = A.count(3), A.count(2), A.count(1)
DP = [
    [[0.0 for k in range(a + b + c + 1)] for j in range(a + b + 1)]
    for i in range(a + 1)
]
for i in range(a + 1):
    for j in range(a - i + b + 1):
        for k in range(a - i + b - j + c + 1):
            if i + j + k == 0:
                continue
            DP[i][j][k] = n
            if i > 0:
                DP[i][j][k] += i * DP[i - 1][j + 1][k]
            if j > 0:
                DP[i][j][k] += j * DP[i][j - 1][k + 1]
            if k > 0:
                DP[i][j][k] += k * DP[i][j][k - 1]
            DP[i][j][k] /= i + j + k
print(DP[a][b][c])
