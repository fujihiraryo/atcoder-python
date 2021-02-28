class Dinic:
    def __init__(self, graph, start, goal, INF=1 << 30):
        n = len(graph)
        self.size = n
        self.graph = graph
        self.start = start
        self.goal = goal
        self.INF = INF

    def bfs(self):
        self.dist = [self.INF] * self.size
        self.dist[self.start] = 0
        queue = [self.start]
        for x in queue:
            for y in self.graph[x]:
                if self.graph[x][y] == 0 or self.dist[y] < self.INF:
                    continue
                self.dist[y] = self.dist[x] + 1
                queue.append(y)

    def dfs(self, x, flow):
        if x == self.goal:
            return flow
        for y in self.graph[x]:
            capa = self.graph[x][y]
            if capa == 0 or self.dist[x] >= self.dist[y] or y in self.checked[x]:
                continue
            self.checked[x].add(y)
            f = self.dfs(y, min(flow, capa))
            if f:
                self.graph[x][y] -= f
                self.graph[y][x] += f
                return f
        return 0

    def max_flow(self):
        res = 0
        while True:
            self.bfs()
            if self.dist[self.goal] == self.INF:
                return res
            flow = self.INF
            self.checked = [set() for _ in range(self.size)]
            while flow:
                flow = self.dfs(self.start, self.INF)
                res += flow


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
                graph[x][start] = 0
            if s[i][j] == "W":
                graph[x][goal] = INF
                graph[goal][x] = 0
        else:
            if s[i][j] == "W":
                graph[start][x] = INF
                graph[x][start] = 0
            if s[i][j] == "B":
                graph[x][goal] = INF
                graph[goal][x] = 0
flow = Dinic(graph, start, goal).max_flow()
print(n * (n - 1) * 2 - flow)
