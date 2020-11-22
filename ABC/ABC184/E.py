import collections

INF = 10 ** 20
h, w = map(int, input().split())
A = [input() for i in range(h)]
D = collections.defaultdict(lambda: set())
for i in range(h):
    for j in range(w):
        if A[i][j] == "S":
            si, sj = i, j
        if A[i][j] == "G":
            gi, gj = i, j
        if A[i][j].islower():
            D[A[i][j]].add((i, j))
C = [[INF for j in range(w)] for i in range(h)]
C[si][sj] = 0
Q = collections.deque([(si, sj)])
while Q:
    i, j = Q.popleft()
    S = set()
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if not (0 <= ni < h and 0 <= nj < w and A[ni][nj] != "#"):
            continue
        S.add((ni, nj))
    if A[i][j].islower():
        S |= D[A[i][j]]
        D[A[i][j]].clear()
    for ni, nj in S:
        if C[i][j] + 1 < C[ni][nj]:
            C[ni][nj] = C[i][j] + 1
            Q.append((ni, nj))
    S.clear()
if C[gi][gj] == INF:
    print(-1)
else:
    print(C[gi][gj])
