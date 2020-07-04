d = int(input())
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]
X = []
L = [-1 for j in range(26)]
for i in range(d):
    max_diff = -10**10
    best_j = 0
    for j in range(26):
        memo = L[j]
        L[j] = i
        diff = S[i][j] - sum([C[jj] * (i - L[jj]) for jj in range(26)])
        if diff > max_diff:
            max_diff = diff
            best_j = j
        L[j] = memo
    L[best_j] = i
    X.append(best_j)
for x in X:
    print(x + 1)
