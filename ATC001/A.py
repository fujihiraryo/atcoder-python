H, W = map(int, input().split())
C = [list(input()) for h in range(H)]
for h in range(H):
    for w in range(W):
        if C[h][w] == 's':
            start = (h, w)
        if C[h][w] == 'g':
            goal = (h, w)
V = [[0 for w in range(W)] for h in range(H)]  # visited
Q = [start]  # que
h0, w0 = start
V[h0][w0] = 1
while len(Q) > 0:
    (h0, w0) = Q.pop()
    if (h0, w0) == goal:
        print('Yes')
        exit()
    # (h0,w0)の隣接点を列挙
    N = [(h0, w0 - 1), (h0, w0 + 1), (h0 - 1, w0), (h0 + 1, w0)]
    for (h1, w1) in N:
        if 0 <= h1 < H and 0 <= w1 < W and V[h1][w1] == 0 and C[h1][w1] != '#':
            Q.append((h1, w1))
            V[h1][w1] = 1
print('No')
