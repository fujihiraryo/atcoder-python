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
    if k != 3:
        exit()
    x, y, z = v
    query.append((x - 1, y - 1, z - 1))

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


def lca_dist(x, y):
    u, v = x, y
    if depth[u] > depth[v]:
        u, v = v, u
    d = depth[v] - depth[u]
    for i in range(MAX):
        if (1 << i) & d:
            v = dp[v][i]
    if u == v:
        return u, d
    for i in range(MAX)[::-1]:
        if dp[u][i] == dp[v][i]:
            continue
        u = dp[u][i]
        v = dp[v][i]
        d += 2 ** (i + 1)
    return parent[u], d + 2


for x, y, z in query:
    _, d_xy = lca_dist(x, y)
    _, d_yz = lca_dist(y, z)
    _, d_zx = lca_dist(z, x)
    print((d_xy + d_yz + d_zx) // 2)
