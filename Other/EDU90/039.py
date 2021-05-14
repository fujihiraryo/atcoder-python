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
size = [1] * n
for x in order[::-1]:
    for y in child[x]:
        size[x] += size[y]
ans = sum(size[x] * (n - size[x]) for x in range(n))
print(ans)
