n = int(input())
cnt = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    x = int(str(i)[0])
    y = int(str(i)[-1])
    cnt[x][y] += 1
ans = 0
for x in range(10):
    for y in range(10):
        ans += cnt[x][y] * cnt[y][x]
print(ans)
