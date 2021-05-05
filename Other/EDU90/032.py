INF = 1 << 30
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    b[x - 1][y - 1] = 1
    b[y - 1][x - 1] = 1
dp = [[INF] * n for _ in range(1 << n)]
for i in range(n):
    dp[0][i] = a[i][0]
for s in range(1 << n):
    cnt = bin(s).count("1")
    for i in range(n):
        if (1 << i) & s:
            continue
        for j in range(n):
            if b[i][j] or not (1 << j) & s:
                continue
            dp[s][i] = min(dp[s][i], dp[s - (1 << j)][j] + a[i][cnt])
ans = min(dp[(1 << n) - 1 - (1 << i)][i] for i in range(n))
print(ans if ans < INF else -1)
