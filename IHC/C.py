d = int(input())
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]


def f(X):
    score = 0
    L = [-1 for j in range(26)]
    A = [0 for j in range(26)]
    for i in range(d):
        score += S[i][X[i]]
        A[X[i]] += (i - L[X[i]]) * (i - L[X[i]] - 1) // 2
        L[X[i]] = i
    for j in range(26):
        A[j] += (d - L[j]) * (d - L[j] - 1) // 2
        score -= C[j] * A[j]
    return score


X = [int(input()) - 1 for i in range(d)]
m = int(input())
for k in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())
    X[i] = j
    print(f(X))
