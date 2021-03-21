from collections import deque

h, w = map(int, input().split())
i0, j0 = map(lambda x: int(x) - 1, input().split())
i1, j1 = map(lambda x: int(x) - 1, input().split())
S = [input() for i in range(h)]
D = [[-1] * w for i in range(h)]
Q = deque([(i0, j0, 0)])
while Q:
    i, j, cnt = Q.popleft()
    if D[i][j] != -1:
        continue
    D[i][j] = cnt
    for di in range(-2, 3):
        for dj in range(-2, 3):
            ii, jj = i + di, j + dj
            if 0 <= ii < h and 0 <= jj < w and S[ii][jj] == "." and D[ii][jj] == -1:
                if abs(di) + abs(dj) == 1:
                    Q.appendleft((ii, jj, cnt))
                else:
                    Q.append((ii, jj, cnt + 1))
print(D[i1][j1])
