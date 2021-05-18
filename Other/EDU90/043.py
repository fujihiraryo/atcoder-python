from collections import deque

INF = 10 ** 10
h, w = map(int, input().split())
n = h * w * 4 + 2
rs, cs = map(lambda x: int(x) - 1, input().split())
rt, ct = map(lambda x: int(x) - 1, input().split())
board = [input() for _ in range(h)]
start = h * w * 4
goal = h * w * 4 + 1
dist = [INF] * n
dq = deque()
dq.append(start)
dist[start] = 0
while dq:
    x = dq.popleft()
    i, j, k = x // 4 // w, x // 4 % w, x % 4
    nxt = []
    if x == start:
        nxt.append(((rs * w + cs) * 4 + 0, 0))
        nxt.append(((rs * w + cs) * 4 + 1, 0))
        nxt.append(((rs * w + cs) * 4 + 2, 0))
        nxt.append(((rs * w + cs) * 4 + 3, 0))
    elif x != goal:
        if i == rt and j == ct:
            nxt.append((goal, 0))
        if i - 1 >= 0 and board[i - 1][j] == ".":
            y = ((i - 1) * w + j) * 4 + 0
            nxt.append((y, int(k != 0)))
        if j + 1 < w and board[i][j + 1] == ".":
            y = (i * w + (j + 1)) * 4 + 1
            nxt.append((y, int(k != 1)))
        if i + 1 < h and board[i + 1][j] == ".":
            y = ((i + 1) * w + j) * 4 + 2
            nxt.append((y, int(k != 2)))
        if j - 1 >= 0 and board[i][j - 1] == ".":
            y = (i * w + (j - 1)) * 4 + 3
            nxt.append((y, int(k != 3)))
    for y, d in nxt:
        if dist[x] + d < dist[y]:
            dist[y] = dist[x] + d
            if d:
                dq.append(y)
            else:
                dq.appendleft(y)
print(dist[goal])
