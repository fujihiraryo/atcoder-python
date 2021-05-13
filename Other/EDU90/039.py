n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
# 0を根とする根付き木にする
child = [[] for _ in range(n)]
parent = [None] * n
order = []
queue = [0]
for x in queue:
    order.append(x)
    for y in tree[x]:
        if y == parent[x]:
            continue
        child[x].append(y)
        parent[y] = x
        queue.append(y)
# 木DP
dp = [0] * n
size = [1] * n
for x in order[::-1]:
    for y in child[x]:
        size[x] += size[y]
        dp[x] += dp[y] + size[y]
# 各子を除く場合の計算
dp_ex = [{} for _ in range(n)]
size_ex = [{} for _ in range(n)]
for x in range(n):
    for y in child[x]:
        dp_ex[x][y] = dp[x] - dp[y] - size[y]
        size_ex[x][y] = size[x] - size[y]
# 部分木の更新
for x in order[1:]:
    p = parent[x]
    dp[x] += dp_ex[p][x] + size_ex[p][x]
    size[x] += size_ex[p][x]
    for y in child[x]:
        dp_ex[x][y] += dp_ex[p][x] + size_ex[p][x]
        size_ex[x][y] += size_ex[p][x]
print(sum(dp) // 2)
