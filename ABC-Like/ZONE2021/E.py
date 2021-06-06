import heapq

r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
b = [list(map(int, input().split())) for _ in range(r - 1)]
INF = 1 << 30
dist = [[INF] * c for _ in range(2 * r)]
dist[0][0] = 0
heap = [(0, 0)]
while heap:
    d, x = heapq.heappop(heap)
    i, j = x // c, x % c
    if dist[i][j] < d:
        continue
    if i < r:
        if dist[r + i][j] > dist[i][j] + 1:
            dist[r + i][j] = dist[i][j] + 1
            heapq.heappush(heap, (dist[r + i][j], (r + i) * c + j))
        if i < r - 1 and dist[i + 1][j] > dist[i][j] + b[i][j]:
            dist[i + 1][j] = dist[i][j] + b[i][j]
            heapq.heappush(heap, (dist[i + 1][j], (i + 1) * c + j))
        if j > 0 and dist[i][j - 1] > dist[i][j] + a[i][j - 1]:
            dist[i][j - 1] = dist[i][j] + a[i][j - 1]
            heapq.heappush(heap, (dist[i][j - 1], i * c + j - 1))
        if j < c - 1 and dist[i][j + 1] > dist[i][j] + a[i][j]:
            dist[i][j + 1] = dist[i][j] + a[i][j]
            heapq.heappush(heap, (dist[i][j + 1], i * c + j + 1))
    else:
        if i > r and dist[i - 1][j] > dist[i][j] + 1:
            dist[i - 1][j] = dist[i][j] + 1
            heapq.heappush(heap, (dist[i - 1][j], (i - 1) * c + j))
        if dist[i - r][j] > dist[i][j]:
            dist[i - r][j] = dist[i][j]
            heapq.heappush(heap, (dist[i - r][j], (i - r) * c + j))
print(dist[r - 1][c - 1])
