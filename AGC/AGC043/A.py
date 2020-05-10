h, w = map(int, input().split())
S = [input() for i in range(h)]
DP = [[0 for j in range(w)] for i in range(h)]
if S[0][0] == '#':
    DP[0][0] = 1
for j in range(1, w):
    if S[0][j - 1] == '.' and S[0][j] == '#':
        DP[0][j] = DP[0][j - 1] + 1
    else:
        DP[0][j] = DP[0][j - 1]
for i in range(1, h):
    if S[i - 1][0] == '.' and S[i][0] == '#':
        DP[i][0] = DP[i - 1][0] + 1
    else:
        DP[i][0] = DP[i - 1][0]
    for j in range(1, w):
        if S[i - 1][j] == '.' and S[i][j] == '#':
            up = DP[i - 1][j] + 1
        else:
            up = DP[i - 1][j]
        if S[i][j - 1] == '.' and S[i][j] == '#':
            left = DP[i][j - 1] + 1
        else:
            left = DP[i][j - 1]
        DP[i][j] = min(up, left)
print(DP[-1][-1])
