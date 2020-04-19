# n = int(input())
# *A, = map(int, input().split())
n = 4
A = [10, 20, 30, 40]
DP = [[None for r in range(n+1)] for l in range(n)]
S = [0]
for i in range(n):
    S.append(S[-1]+A[i])


def dp(l, r):
    # 区間[l,r)での最小コスト
    if r <= l+1:
        DP[l][r] = 0
    if DP[l][r] != None:
        return DP[l][r]
    # S[r]-S[l]=sum(A[l:r])
    DP[l][r] = S[r]-S[l]+min([dp(l, i)+dp(i, r) for i in range(l+1, r)])
    return DP[l][r]


print(dp(0, n))
