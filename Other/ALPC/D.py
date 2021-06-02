def max_flow(graph, s, t):
    global INF
    n = len(graph)
    adj = [[] for _ in range(n)]
    cap = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in graph[x]:
            adj[x].append(y)
            adj[y].append(x)
            cap[x][y] = graph[x][y]
    tot = 0
    while True:
        # bfs
        level = [INF] * n
        level[s] = 0
        queue = [s]
        for x in queue:
            for y in adj[x]:
                if cap[x][y] == 0 or level[y] < INF:
                    continue
                level[y] = level[x] + 1
                queue.append(y)
        if level[t] == INF:
            break
        cur = [0] * n
        while True:
            # dfs
            stack = [s]
            prev = [None] * n
            while stack:
                x = stack[-1]
                if x == t:
                    break
                for y in adj[x][cur[x] :]:
                    if cap[x][y] == 0 or level[x] >= level[y]:
                        cur[x] += 1
                        continue
                    stack.append(y)
                    prev[y] = x
                    break
                else:
                    stack.pop()
                    level[x] = 0
            else:
                break
            # 経路復元
            f = INF
            y = t
            while y != s:
                x = prev[y]
                f = min(f, cap[x][y])
                y = x
            if f == 0:
                break
            # 残容量更新
            y = t
            while y != s:
                x = prev[y]
                cap[x][y] -= f
                cap[y][x] += f
                y = x
            tot += f
    flow = [{} for _ in range(n)]
    for x in range(n):
        for y in graph[x]:
            if cap[y][x]:
                flow[x][y] = cap[y][x]
    return flow, tot


INF = 1 << 60
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
graph = [{} for _ in range(n * m + 2)]
s = n * m
t = n * m + 1
for i in range(n):
    for j in range(m):
        if board[i][j] == "#":
            continue
        x = i * m + j
        if (i + j) % 2 == 0:
            graph[s][x] = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + di < n and 0 <= j + dj < m and board[i + di][j + dj] == ".":
                    y = (i + di) * m + j + dj
                    graph[x][y] = 1
        else:
            graph[x][t] = 1
flow, tot = max_flow(graph, s, t)
print(tot)
for i in range(n):
    for j in range(m):
        x = i * m + j
        if (i + j) % 2 == 0:
            for y in flow[x]:
                di, dj = y // m - i, y % m - j
                if di == -1:
                    board[i][j] = "^"
                    board[i + di][j + dj] = "v"
                if di == 1:
                    board[i][j] = "v"
                    board[i + di][j + dj] = "^"
                if dj == -1:
                    board[i][j] = "<"
                    board[i + di][j + dj] = ">"
                if dj == 1:
                    board[i][j] = ">"
                    board[i + di][j + dj] = "<"
for i in range(n):
    print("".join(board[i]))
