h, w = map(int, input().split())
p = 10**9+7
S = [input() for i in range(h)]
DP = [[0 for j in range(w)] for i in range(h)]
DP[0][0] = 1
for i in range(h):
    for j in range(w):
        if i > 0 and S[i-1][j] == '.':
            DP[i][j] += DP[i-1][j]
        if j > 0 and S[i][j-1] == '.':
            DP[i][j] += DP[i][j-1]
        DP[i][j] %= p
print(DP[h-1][w-1])
