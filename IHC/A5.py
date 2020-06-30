# 貪欲+山登り(日付だけランダム)
import time
import random

d = int(input())
dd = d * (d + 1) // 2
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]
T = []
L = [-1 for j in range(26)]
for i in range(d):
    max_diff = -10**7
    arg_max = 0
    for j in range(26):
        memo = L[j]
        L[j] = i
        diff = S[i][j] - sum([C[k] * (i - L[k]) for k in range(26)])
        if diff > max_diff:
            max_diff = diff
            arg_max = j
        L[j] = memo
    T.append(arg_max)
    L[arg_max] = i


def calc_score(T):
    L = [-1 for j in range(26)]
    X = [0 for j in range(26)]
    score = 0
    for i in range(d):
        score += S[i][T[i]]
        X[T[i]] += (d - i) * (i - L[T[i]])
        L[T[i]] = i
    for j in range(26):
        score -= C[j] * (dd - X[j])
    return score


score = calc_score(T)
start = time.time()
while True:
    now = time.time()
    if now - start > 1.8:
        break
    i = random.choice(range(d))
    arg_max = 0
    max_diff = 0
    for j in range(26):
        memo = T[i]
        T[i] = j
        new_score = calc_score(T)
        if new_score - score > max_diff:
            max_diff = new_score - score
            arg_max = j
        T[i] = memo
    if max_diff > 0:
        T[i] = arg_max
        score += max_diff

for t in T:
    print(t + 1)
