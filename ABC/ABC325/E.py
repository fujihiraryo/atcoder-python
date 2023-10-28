import heapq

n, a, b, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
graph0 = [[0] * n for _ in range(n)]
graph1 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph0[i][j] = d[i][j] * a
        graph1[i][j] = d[i][j] * b + c

dist0 = [10**30] * n
dist1 = [10**30] * n
dist0[0] = 0
dist1[0] = 0
heap = [(0, 0, 0)]  # 車だけのルート、電車あり、訪問先
heapq.heapify(heap)
while heap:
    d0, d1, x = heapq.heappop(heap)
    if dist0[x] < d0 and dist1[x] < d1:
        continue
    for y in range(n):
        flag = False
        if dist0[y] > dist0[x] + graph0[x][y]:
            dist0[y] = dist0[x] + graph0[x][y]
            flag = True
        if dist1[y] > dist0[x] + min(graph0[x][y], graph1[x][y]):
            dist1[y] = dist0[x] + min(graph0[x][y], graph1[x][y])
            flag = True
        if dist1[y] > dist1[x] + graph1[x][y]:
            dist1[y] = dist1[x] + graph1[x][y]
            flag = True
        if flag:
            heapq.heappush(heap, (dist0[y], dist1[y], y))
print(dist1[n - 1])
