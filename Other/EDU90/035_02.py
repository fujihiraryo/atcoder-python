MAX = 21
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
q = int(input())
query = []
for _ in range(q):
    k, *v, = map(int, input().split())
    if k != 2:
        exit()
    x, y = v
    query.append((x - 1, y - 1))

parent = [0] * n
depth = [0] * n
stack = [0]
while stack:
    x = stack.pop()
    for y in tree[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        depth[y] = depth[x] + 1
        stack.append(y)

dp = [[0] * MAX for _ in range(n)]
for j in range(MAX):
    for x in range(n):
        if j == 0:
            dp[x][j] = parent[x]
        else:
            dp[x][j] = dp[dp[x][j - 1]][j - 1]

for x, y in query:
    if depth[x] > depth[y]:
        x, y = y, x
    d = depth[y] - depth[x]
    for i in range(MAX):
        if (1 << i) & d:
            y = dp[y][i]
    if x == y:
        print(d)
        continue
    ans = d
    for i in range(MAX)[::-1]:
        if dp[x][i] == dp[y][i]:
            continue
        x = dp[x][i]
        y = dp[y][i]
        ans += 2 ** (i + 1)
    print(ans + 2)
