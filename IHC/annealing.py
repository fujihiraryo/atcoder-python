from random import choice
from random import random
from time import time
start_time = time()
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


max_score = f(X)
while time() - start_time < 1.8:
    t = (time() - start_time) / 2
    i = choice(range(d))
    j = choice(range(26))
    memo = X[i]
    X[i] = j
    score = f(X)
    if score > max_score:
        max_score = score
    elif random() < pow(2.7, (score - max_score) / pow(2000, 1 - t)):
        max_score = score
    else:
        X[i] = memo
    a = choice(range(7))
    i0 = choice(range(d - a))
    i1 = i0 + a
    memo = X[i0], X[i1]
    X[i0], X[i1] = X[i1], X[i0]
    score = f(X)
    if score > max_score:
        max_score = score
    elif random() < pow(2.7, (score - max_score) / pow(2000, 1 - t)):
        max_score = score
    else:
        X[i0], X[i1] = memo
for x in X:
    print(x + 1)
