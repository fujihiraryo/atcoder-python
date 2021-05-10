n = int(input())
if n > 5000:
    exit()
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

parent = [0] * n
order = []
stack = [0]
while stack:
    x = stack.pop()
    order.append(x)
    for y in tree[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

for _ in range(int(input())):
    k, *v, = map(int, input().split())
    mark = [0] * n
    for x in v:
        mark[x - 1] = 1
    dp = [0] * n
    for x in order[::-1]:
        dp[x] = mark[x]
        for y in tree[x]:
            if y == parent[x]:
                continue
            dp[x] += dp[y]
    ans = 0
    for c in dp:
        if c == 0 or c == k:
            continue
        ans += 1
    print(ans)
