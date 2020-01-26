"""
N M
V[0] W[0]
...
V[N-1] W[N-1]
という入力が与えられたとき,
Wの合計がMを超えないようにVの合計を最大化する.
"""

import numpy as np
N, M = map(int, input().split())
VW = [tuple(map(int, input().split())) for n in range(N)]
VW.sort(key=lambda x: x[1])
DP = np.zeros(M + 1, dtype=int)
# DP[m]はM=mのときの答え
for v, w in VW:
    np.maximum(DP[:-w] + v, DP[w:], out=DP[w:])
    print(DP)
print(DP[M])
