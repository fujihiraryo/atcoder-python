import copy

n, m = map(int, input().split())
from_set = [set() for _ in range(n)]
to_set = [set() for _ in range(n)]
stack = set(range(n))
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    from_set[y].add(x)
    to_set[x].add(y)
    if y in stack:
        stack.remove(y)
_from_set = copy.deepcopy(from_set)
# トポロジカルソート
order = []
while stack:
    x = stack.pop()
    order.append(x)
    while to_set[x]:
        y = to_set[x].pop()
        from_set[y].remove(x)
        if from_set[y]:
            continue
        stack.add(y)
# 最長パス
from_set = _from_set
dp = [0] * n
for i in order:
    for j in from_set[i]:
        dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
