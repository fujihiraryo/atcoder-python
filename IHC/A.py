import random
import time

d = int(input())
dd = d * (d + 1) // 2
(*C,) = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]


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


# 各日に一番満足度の増加が大きいコンテストを開催する
T = [S[i].index(max(S[i])) for i in range(d)]
score = calc_score(T)
start = time.time()
cnt = 0
while True:
    now = time.time()
    if now - start > 1.8:
        break
    p = (cnt // 26) % d
    q = cnt % 26
    memo = T[p]
    T[p] = q
    new_score = calc_score(T)
    temp = 20000 * (1 - (now - start) / 2)
    prob = 2 ** ((new_score - score) / temp)
    if random.random() < prob:
        score = new_score
    else:
        T[p] = memo
    cnt = (cnt + 1) % (10 ** 9 + 7)

for t in T:
    print(t + 1)
