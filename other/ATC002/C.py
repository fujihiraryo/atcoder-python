N = int(input())
(*W,) = map(int, input().split())
S = [0]
inf = 10 ** 10
for n in range(N):
    S.append(S[-1] + W[n])
C = [[inf for m in range(N + 1)] for n in range(N)]


def f(i, j):
    # W[i:j]で作る二分木の最小コスト
    if j - i == 1:
        C[i][j] = 0
    elif C[i][j] == inf:
        for k in range(i + 1, j):
            C[i][j] = min(f(i, k) + f(k, j) + S[j] - S[i], C[i][j])
    return C[i][j]


print(f(0, N))
