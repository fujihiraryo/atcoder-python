class Dinic:
    def __init__(self, graph, start, goal, INF=1 << 30):
        n = len(graph)
        self.size = n
        self.graph = [{} for _ in range(n)]
        for x in range(n):
            for y in graph[x]:
                self.graph[x][y] = graph[x][y]
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
n, w = map(int, input().split())
*a, = map(int, input().split())
graph = [{} for _ in range(n + 2)]
for i in range(n):
    graph[n][i] = a[i]
    graph[i][n] = 0
    graph[i][n + 1] = w
    graph[n + 1][i] = 0
for i in range(n):
    k, *lst, = map(int, input().split())
    for j in lst:
        graph[j - 1][i] = INF
        graph[i][j - 1] = 0
ans = sum(a) - Dinic(graph, n, n + 1).max_flow()
print(ans)
