S = input()
T = input()
m, n = len(S), len(T)
DP = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if S[i-1] == T[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j])
i, j = m, n
X = ''
while len(X) < DP[m][n]:
    if S[i-1] == T[j-1]:
        X = S[i-1] + X
        i -= 1
        j -= 1
    elif DP[i][j] == DP[i-1][j]:
        i -= 1
    elif DP[i][j] == DP[i][j]:
        j -= 1
print(X)
