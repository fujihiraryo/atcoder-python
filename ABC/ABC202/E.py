import bisect
import sys

sys.setrecursionlimit(10 ** 6)

int0 = lambda x: int(x) - 1
n = int(input())
*p, = map(int0, input().split())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    tree[p[i]].append(i + 1)

arrived_at = [0] * n
left_at = [0] * n
depth = [0] * n
time = 0


def dfs(x):
    global time
    arrived_at[x] = time
    time += 1
    for y in tree[x]:
        depth[y] = depth[x] + 1
        dfs(y)
    left_at[x] = time
    time += 1


dfs(0)

lst = [[] for _ in range(n)]
for x in range(n):
    lst[depth[x]].append(arrived_at[x])
for l in lst:
    l.sort()

q = int(input())
for _ in range(q):
    u, d = map(int, input().split())
    u -= 1
    i = bisect.bisect_left(lst[d], arrived_at[u])
    j = bisect.bisect_right(lst[d], left_at[u])
    print(j - i)
