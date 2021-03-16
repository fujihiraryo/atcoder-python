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


def minimum_cost_flow(graph, start, goal, flow):
    n = len(graph)
    residual_graph = [{} for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            residual_graph[i][j] = graph[i][j]
    INF = 1 << 30
    residual_flow = flow
    min_cost = 0
    while residual_flow:
        # find path
        path_cost = [INF] * n
        path_cost[start] = 0
        last = [None] * n
        update = True
        while update:
            update = False
            for i in range(n):
                if path_cost[i] == INF:
                    continue
                for j in residual_graph[i]:
                    capa, cost = residual_graph[i][j]
                    if capa > 0 and path_cost[j] > path_cost[i] + cost:
                        path_cost[j] = path_cost[i] + cost
                        last[j] = i
                        update = True
        if path_cost[goal] == INF:
            return None
        # min capacity
        min_capa = residual_flow
        x = goal
        while x != start:
            capa, _ = residual_graph[last[x]][x]
            min_capa = min(min_capa, capa)
            x = last[x]
        residual_flow -= min_capa
        min_cost += min_capa * path_cost[goal]
        # update graph
        x = goal
        while x != start:
            capa, cost = residual_graph[last[x]][x]
            residual_graph[last[x]][x] = (capa - min_capa, cost)
            capa, cost = residual_graph[x][last[x]]
            residual_graph[x][last[x]] = (capa + min_capa, cost)
            x = last[x]
    return min_cost


def weighted_bipartite_matching(bigraph):
    nx = len(bigraph)
    ny = 0
    max_weight = 0
    for x in range(nx):
        for y in bigraph[x]:
            ny = max(ny, y + 1)
            max_weight = max(max_weight, bigraph[x][y])
    graph = [{} for _ in range(nx + ny + 2)]
    for x in range(nx):
        graph[0][x + 1] = (1, 0)
        graph[x + 1][0] = (0, 0)
    for x in range(nx):
        for y in bigraph[x]:
            graph[x + 1][y + nx + 1] = (1, max_weight - bigraph[x][y])
            graph[y + nx + 1][x + 1] = (0, bigraph[x][y] - max_weight)
    for y in range(ny):
        graph[y + nx + 1][nx + ny + 1] = (1, 0)
        graph[nx + ny + 1][y + nx + 1] = (0, 0)
    capa_graph = [{} for _ in range(nx + ny + 2)]
    for x in range(nx + ny + 2):
        for y in graph[x]:
            capa, _ = graph[x][y]
            capa_graph[x][y] = capa
    max_flow = Dinic(capa_graph, 0, nx + ny + 1).max_flow()
    min_cost = minimum_cost_flow(graph, 0, nx + ny + 1, max_flow)
    return max_flow * max_weight - min_cost


n, m, q = map(int, input().split())
w, v = [], []
for _ in range(n):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)
(*x,) = map(int, input().split())
for _ in range(q):
    bigraph = [{} for _ in range(n)]
    j0, j1 = map(int, input().split())
    for i in range(n):
        for j in range(m):
            if j0 - 1 <= j <= j1 - 1:
                continue
            if w[i] <= x[j]:
                bigraph[i][j] = v[i]
    ans = weighted_bipartite_matching(bigraph)
    print(ans)
