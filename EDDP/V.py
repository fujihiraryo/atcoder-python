n, m = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)
# 0を根とする根付き木にする
child = [[] for _ in range(n)]
parent = [None] * n
order = []
que = [0]
for x in que:
    order.append(x)
    for y in tree[x]:
        if y == parent[x]:
            continue
        child[x].append(y)
        parent[y] = x
        que.append(y)
# 葉から順にx以下の部分木の計算
dp0 = [1] * n
dp1 = [{} for _ in range(n)]
for x in order[::-1]:
    size = len(child[x])
    left, right = [1], [1]
    for i in range(size):
        left.append(left[-1] * (1 + dp0[child[x][i]]) % m)
        right.append(right[-1] * (1 + dp0[child[x][size - 1 - i]]) % m)
    right.reverse()
    dp0[x] = left[size]
    for i in range(size):
        dp1[x][child[x][i]] = left[i] * right[i + 1] % m
# 根から順にxを根とする場合の計算
for x in order[1:]:
    dp0[x] = dp0[x] * (1 + dp1[parent[x]][x]) % m
    for y in child[x]:
        dp1[x][y] = dp1[x][y] * (1 + dp1[parent[x]][x]) % m
print(*dp0, sep="\n")
