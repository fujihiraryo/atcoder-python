from collections import deque
inf = 10**18
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1
A = [list(input()) for r in range(R)]
V = [[inf for c in range(C)] for r in range(R)]
Q = deque([(sy, sx)])
V[sy][sx] = 0
while len(Q) != 0:
    y, x = Q.popleft()
    if (y, x) == (gy, gx):
        print(V[y][x])
        exit()
    N = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
    for (y1, x1) in N:
        if A[y1][x1] != '#' and V[y1][x1] == inf:
            Q.append((y1, x1))
            V[y1][x1] = V[y][x] + 1
