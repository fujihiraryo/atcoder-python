n, m = map(int, input().split())
from_list = [[] for _ in range(n)]
to_list = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    from_list[y].append(x)
    to_list[x].append(y)
# トポロジカルソート
from_set = [set(from_list[x]) for x in range(n)]
stack = [x for x in range(n) if len(from_list[x]) == 0]
order = []
while stack:
    x = stack.pop()
    order.append(x)
    while to_list[x]:
        y = to_list[x].pop()
        from_set[y].remove(x)
        if from_set[y]:
            continue
        stack.append(y)
# 最長パス
dp = [0] * n
for i in order:
    for j in from_list[i]:
        dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
