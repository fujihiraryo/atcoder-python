"""
N M
V[0] W[0]
...
V[N-1] W[N-1]
という入力が与えられたとき,
Wの合計がMを超えないようにVの合計を最大化する.
"""

N, M = map(int, input().split())
V = []
W = []
for n in range(N):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)

dp = [[0 for w in range(M + 1)] for n in range(N + 1)]
# dp[n][m] = (N=n, M=mとしたときのこの問題の答え)

for n in range(N):
    for m in range(M+1):
        dp[n + 1][m] = max(dp[n][m], dp[n][max(m - W[n], 0)] + V[n])

print(dp[N][M])
