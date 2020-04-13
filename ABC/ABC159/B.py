S = list(input())
N = len(S)
S0 = S[:(N - 1) // 2]
S1 = S[(N + 1) // 2:]
if S0 == S0[::-1] and S1 == S1[::-1] and S == S[::-1]:
    print('Yes')
else:
    print('No')
