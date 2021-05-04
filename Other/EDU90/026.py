n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
stack = [0]
color = [None] * n
color[0] = 0
while stack:
    x = stack.pop()
    for y in tree[x]:
        if color[y] is not None:
            continue
        color[y] = color[x] ^ 1
        stack.append(y)
a = 0 if color.count(0) >= n // 2 else 1
print(*[x + 1 for x in range(n) if color[x] == a][: n // 2])
