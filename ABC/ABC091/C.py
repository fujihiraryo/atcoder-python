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


def bipartite_matching(bigraph):
    nx = len(bigraph)
    ny = 0
    for x in range(nx):
        for y in bigraph[x]:
            ny = max(ny, y + 1)
    graph = [{} for _ in range(nx + ny + 2)]
    for x in range(nx):
        graph[0][x + 1] = 1
        graph[x + 1][0] = 0
    for x in range(nx):
        for y in bigraph[x]:
            graph[x + 1][y + nx + 1] = 1
            graph[y + nx + 1][x + 1] = 0
    for y in range(ny):
        graph[y + nx + 1][nx + ny + 1] = 1
        graph[nx + ny + 1][y + nx + 1] = 0
    return Dinic(graph, 0, nx + ny + 1).max_flow()


n = int(input())
x = [tuple(map(int, input().split())) for _ in range(n)]
y = [tuple(map(int, input().split())) for _ in range(n)]
bigraph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if x[i][0] < y[j][0] and x[i][1] < y[j][1]:
            bigraph[i].append(j)
print(bipartite_matching(bigraph))
