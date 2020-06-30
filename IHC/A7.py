# 貪欲のみ(日付を2つ)
d = int(input())
*C, = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]
T = []
L = [-1 for j in range(26)]
for i in range(d - 1):
    i0, i1 = i, i + 1
    max_diff = -10**7
    arg_max = 0
    for j0 in range(26):
        memo0 = L[j0]
        for j1 in range(26):
            memo1 = L[j1]
            L[j0], L[j1] = i0, i1
            diff = S[i][j] - sum([C[k] * (i - L[k]) for k in range(26)])
            if diff > max_diff:
                max_diff = diff
                arg_max = j
            L[j] = memo
    T.append(arg_max)
    L[arg_max] = i
for t in T:
    print(t + 1)
