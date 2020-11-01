import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

H, W = map(int, input().split())
S = []
for h in range(H):
    Sh = list(input())
    S.append(Sh)
G = [[0 for _ in range(H * W)] for _ in range(H * W)]
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            if h > 0 and S[h - 1][w] == ".":
                G[h * W + w][(h - 1) * W + w] = 1
                G[(h - 1) * W + w][h * W + w] = 1
            if w > 0 and S[h][w - 1] == ".":
                G[h * W + w][h * W + (w - 1)] = 1
                G[h * W + (w - 1)][h * W + w] = 1
            if h < H - 1 and S[h + 1][w] == ".":
                G[h * W + w][(h + 1) * W + w] = 1
                G[(h + 1) * W + w][h * W + w] = 1
            if w < W - 1 and S[h][w + 1] == ".":
                G[h * W + w][h * W + (w + 1)] = 1
                G[h * W + (w + 1)][h * W + w] = 1
graph = csr_matrix(G)
dist_matrix = floyd_warshall(csgraph=graph, directed=False)
max_dist = 0
for i in range(H * W):
    for j in range(H * W):
        d = dist_matrix[i][j]
        if d != np.inf and d > max_dist:
            max_dist = d
print(int(max_dist))
