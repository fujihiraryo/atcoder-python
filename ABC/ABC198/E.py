import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())
(*c,) = map(int, input().split())
c = [c[i] - 1 for i in range(n)]
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
visited = [0] * n
cnt = [0] * (max(c) + 1)
ans = []


def dfs(x):
    visited[x] = 1
    if cnt[c[x]] == 0:
        ans.append(x)
    cnt[c[x]] += 1
    for y in tree[x]:
        if visited[y]:
            continue
        dfs(y)
    cnt[c[x]] -= 1


dfs(0)
ans.sort()
for x in ans:
    print(x + 1)
