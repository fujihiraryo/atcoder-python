int0 = lambda x: int(x) - 1
n = int(input())
*c, = map(int0, input().split())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int0, input().split())
    edge[a].append(b)
    edge[b].append(a)

# dfs
visited = [0] * n
cnt = [0] * (max(c) + 1)
ans = []
stack = [0]
while stack:
    x = stack.pop()
    if visited[x]:
        # 帰りがけ
        cnt[c[x]] -= 1
        continue
    visited[x] = 1
    if cnt[c[x]] == 0:
        ans.append(x)
    cnt[c[x]] += 1
    stack.append(x)
    for y in edge[x]:
        if visited[y]:
            continue
        stack.append(y)

ans.sort()
print(*[x + 1 for x in ans], sep="\n")
