d = int(input())
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]
T = [int(input()) - 1 for i in range(d)]
L = [-1 for j in range(26)]
score = 0
for i in range(d):
    score += S[i][T[i]]
    L[T[i]] = i
    score -= sum([C[j] * (i - L[j]) for j in range(26)])
    print(score)
