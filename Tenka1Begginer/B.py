N = int(input())
S = list(input())
K = int(input())
target = S[K - 1]
for i in range(N):
    if S[i] != target:
        S[i] = '*'
print(''.join(S))