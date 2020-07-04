d = int(input())
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]
X = [int(input()) - 1 for i in range(d)]
L = [-1 for j in range(26)]
score = 0
for i in range(d):
    L[X[i]] = i
    score += S[i][X[i]]
    score -= sum([C[j] * (i - L[j]) for j in range(26)])
    print(score)
