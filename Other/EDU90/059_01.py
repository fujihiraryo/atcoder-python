int0 = lambda x: int(x) - 1
n, m, q = map(int, input().split())
if max(n, m, q) > 2000:
    exit()
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int0, input().split())
    graph[x].append(y)
dp = [set() for _ in range(n)]
for i in range(n):
    stack = [i]
    while stack:
        x = stack.pop()
        dp[i].add(x)
        for y in graph[x]:
            if y in dp[i]:
                continue
            stack.append(y)
for _ in range(q):
    a, b = map(int0, input().split())
    print("Yes" if b in dp[a] else "No")
