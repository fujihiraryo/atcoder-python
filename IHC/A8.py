# 貪欲+山登り(2点交換+1点更新)
import time
import random

d = int(input())
dd = d * (d + 1) // 2
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]

# 貪欲法による初期解の構築
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
    # 1点更新
    i = random.choice(range(d))
    j = random.choice(range(26))
    memo = T[i]
    T[i] = j
    new_score = calc_score(T)
    T[i] = memo
    if new_score > score:
        T[i] = j
        score = new_score
    # 2点交換
    i0 = random.choice(range(d))
    z = random.choice(range(10))
    i1 = i0 - z if i0 > z else i0 + z
    T[i0], T[i1] = T[i1], T[i0]
    new_score = calc_score(T)
    T[i0], T[i1] = T[i1], T[i0]
    if new_score > score:
        T[i0], T[i1] = T[i1], T[i0]
        score = new_score
for t in T:
    print(t + 1)
