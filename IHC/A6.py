# 貪欲のみ
d = int(input())
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
for t in T:
    print(t + 1)
