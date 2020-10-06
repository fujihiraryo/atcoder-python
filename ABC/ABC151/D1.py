def grid2graph(grid):
    # .が道で#が壁のグリッドをグラフに変換する
    H, W = len(grid), len(grid[0])
    f = {}
    cnt = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == ".":
                f[(h, w)] = cnt
                cnt += 1
    G = [[] for i in range(cnt)]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                continue
            i = f[(h, w)]
            if 0 <= h - 1 and grid[h - 1][w] == ".":
                j = f[(h - 1, w)]
                G[i].append(j)
            if 0 <= w - 1 and grid[h][w - 1] == ".":
                j = f[(h, w - 1)]
                G[i].append(j)
            if h + 1 < H and grid[h + 1][w] == ".":
                j = f[(h + 1, w)]
                G[i].append(j)
            if w + 1 < W and grid[h][w + 1] == ".":
                j = f[(h, w + 1)]
                G[i].append(j)
    return G


def warshall_floyd(G):
    inf = 10 ** 18
    n = len(G)
    d = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][i] = 0
        for j in G[i]:
            d[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(list(input()))
G = grid2graph(S)
d = warshall_floyd(G)
n = len(d)
ans = 0
for i in range(n - 1):
    for j in range(n):
        ans = max(ans, d[i][j])
print(ans)
