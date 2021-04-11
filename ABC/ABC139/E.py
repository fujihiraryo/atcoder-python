n = int(input())
# 試合番号
num = [[None] * n for _ in range(n)]
size = 0
for i in range(n):
    for j in range(n):
        if i < j:
            num[i][j] = size
            num[j][i] = size
            size += 1
# グラフ構築
to_list = [[] for _ in range(size)]
from_list = [[] for _ in range(size)]
for i in range(n):
    (*a,) = map(lambda x: int(x) - 1, input().split())
    for x, y in zip(a[:-1], a[1:]):
        to_list[num[i][x]].append(num[i][y])
        from_list[num[i][y]].append(num[i][x])
# トポロジカルソート
stack = [i for i in range(size) if len(from_list[i]) == 0]
from_set = [set(from_list[i]) for i in range(size)]
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
if len(order) < size:
    print(-1)
    exit()
# 最長パス
dp = [0] * size
for i in order:
    for j in from_list[i]:
        dp[i] = max(dp[i], dp[j] + 1)
print(max(dp) + 1)
