n = int(input())
*p, = map(int, input().split())
child = [[] for _ in range(n)]
for i in range(n - 1):
    child[p[i] - 1].append(i + 1)

stack = [0]
order = []
while stack:
    x = stack.pop()
    order.append(x)
    for y in child[x]:
        stack.append(y)

dp = [1] * n
size = [1] * n
for x in order[::-1]:
    lst0, lst1, lst2 = [], [], []
    for y in child[x]:
        if size[y] % 2 == 0 and dp[y] < 0:
            lst0.append(y)
        elif size[y] % 2 == 1:
            lst1.append(y)
        else:
            lst2.append(y)
        size[x] += size[y]
    lst1.sort(key=lambda y: dp[y])
    for y in lst0:
        dp[x] += dp[y]
    for i, y in enumerate(lst1):
        dp[x] += (1, -1)[i % 2] * dp[y]
    sgn = (1, -1)[len(lst1) % 2]
    for y in lst2:
        dp[x] += sgn * dp[y]
print((dp[0] + size[0]) // 2)
