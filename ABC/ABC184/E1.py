import collections

INF = 10 ** 20
h, w = map(int, input().split())
A = [input() for i in range(h)]
D = collections.defaultdict(lambda: [])
for i in range(h):
    for j in range(w):
        if A[i][j] == "S":
            si, sj = i, j
        if A[i][j] == "G":
            gi, gj = i, j
        if A[i][j].islower():
            D[A[i][j]].append((i, j))
C = [[INF for j in range(w)] for i in range(h)]
C[si][sj] = 0
Q = collections.deque([(si, sj)])
while Q:
    i, j = Q.popleft()
    for ni, nj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)] + D[A[i][j]]:
        if not (0 <= ni < h and 0 <= nj < w and A[ni][nj] != "#"):
            continue
        if C[i][j] + 1 < C[ni][nj]:
            C[ni][nj] = C[i][j] + 1
            Q.append((ni, nj))
    D[A[i][j]].clear()
if C[gi][gj] == INF:
    print(-1)
else:
    print(C[gi][gj])
