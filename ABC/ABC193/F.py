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
    res = 0
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
            res += f
    return res


INF = 10 ** 10
n = int(input())
s = [input() for _ in range(n)]
graph = [{} for _ in range(n ** 2 + 2)]
start = n ** 2
goal = n ** 2 + 1
for i in range(n):
    for j in range(n):
        x = i * n + j
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i + di < n and 0 <= j + dj < n:
                y = (i + di) * n + j + dj
                graph[x][y] = 1
        if (i + j) % 2:
            if s[i][j] == "B":
                graph[start][x] = INF
            if s[i][j] == "W":
                graph[x][goal] = INF
        else:
            if s[i][j] == "W":
                graph[start][x] = INF
            if s[i][j] == "B":
                graph[x][goal] = INF
print(n * (n - 1) * 2 - max_flow(graph, start, goal))
