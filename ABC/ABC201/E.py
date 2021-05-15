MOD = 10 ** 9 + 7
n = int(input())
tree = [{} for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a - 1][b - 1] = w
    tree[b - 1][a - 1] = w
dist = [0] * n
stack = [0]
visited = [0] * n
while stack:
    x = stack.pop()
    visited[x] = 1
    for y in tree[x]:
        if visited[y]:
            continue
        dist[y] = dist[x] ^ tree[x][y]
        stack.append(y)
ans = 0
for i in range(60):
    cnt = 0
    for x in range(n):
        if dist[x] & (1 << i):
            cnt += 1
    ans += cnt * (n - cnt) * pow(2, i, MOD) % MOD
    ans %= MOD
print(ans)
