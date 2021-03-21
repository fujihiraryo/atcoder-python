n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n - 1):
    xi, yi = xy[i]
    for j in range(i + 1, n):
        xj, yj = xy[j]
        if abs(yi - yj) <= abs(xi - xj):
            cnt += 1
print(cnt)
