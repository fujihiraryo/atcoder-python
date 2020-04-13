S = input()
T = input()
m, n = len(S), len(T)
C = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(m):
    for j in range(n):
        if S[i] == T[j]:
            C[i+1][j+1] = C[i][j] + 1
        else:
            C[i+1][j+1] = max(C[i][j+1], C[i+1][j])
l = C[m][n]
X = ''
while l:
    if S[m-1] == T[n-1]:
        X = S[m-1]+X
        m -= 1
        n -= 1
        l -= 1
    elif C[m][n] == C[m-1][n]:
        m -= 1
    else:
        n -= 1
print(X)
