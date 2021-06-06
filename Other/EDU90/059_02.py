int0 = lambda x: int(x) - 1
n, m, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int0, input().split())
    graph[x].append(y)

query = []
for cnt in range(q):
    x, y = map(int0, input().split())
    query.append((x, y))
    if cnt % 10000 == 0 or cnt == q - 1:
        dp = [0] * n
        for i, (x, _) in enumerate(query):
            dp[x] |= 1 << i
        for x in range(n):
            for y in graph[x]:
                dp[y] |= dp[x]
        for i, (_, y) in enumerate(query):
            print("Yes" if dp[y] >> i & 1 else "No")
        query = []
