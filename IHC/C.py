d = int(input())
dd = d * (d + 1) // 2
*C, = map(int, input().split())
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


T = [int(input()) - 1 for i in range(d)]
m = int(input())
PQ = [tuple(map(int, input().split())) for k in range(m)]
PQ = [(p - 1, q - 1) for p, q in PQ]

for p, q in PQ:
    T[p] = q
    print(calc_score(T))
