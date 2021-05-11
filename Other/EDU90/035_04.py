import sys

sys.setrecursionlimit(10 ** 5)

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
    query.append([x - 1 for x in v])


def dfs(x):
    global parent, depth, arrived_at, time
    arrived_at[x] = time
    time += 1
    for y in tree[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        depth[y] = depth[x] + 1
        dfs(y)


# dfs
parent = [0] * n
depth = [0] * n
arrived_at = [None] * n
time = 0
dfs(0)

# doubling
dp = [[0] * MAX for _ in range(n)]
for j in range(MAX):
    for x in range(n):
        if j == 0:
            dp[x][j] = parent[x]
        else:
            dp[x][j] = dp[dp[x][j - 1]][j - 1]


def dist(x, y):
    if depth[x] > depth[y]:
        x, y = y, x
    d = depth[y] - depth[x]
    for i in range(MAX):
        if (1 << i) & d:
            y = dp[y][i]
    if x == y:
        return d
    for i in range(MAX)[::-1]:
        if dp[x][i] == dp[y][i]:
            continue
        x = dp[x][i]
        y = dp[y][i]
        d += 2 ** (i + 1)
    return d + 2


for lst in query:
    lst.sort(key=lambda x: arrived_at[x])
    ans = 0
    for i in range(len(lst) - 1):
        x, y = lst[i], lst[i + 1]
        ans += dist(x, y)
    ans += dist(lst[-1], lst[0])
    print(ans // 2)
