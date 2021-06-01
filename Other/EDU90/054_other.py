INF = 10 ** 10
int0 = lambda x: int(x) - 1
n, m = map(int, input().split())
graph = [[] for _ in range(m + n)]
for i in range(m):
    input()
    for x in map(int0, input().split()):
        graph[x].append(n + i)
        graph[n + i].append(x)
number = [-2] * (n + m)
number[0] = 0
queue = [0]
for x in queue:
    for y in graph[x]:
        if number[y] != -2:
            continue
        queue.append(y)
        number[y] = number[x] + 1
print(*[x // 2 for x in number[:n]])
