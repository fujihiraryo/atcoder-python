n = int(input())
XY = []
for i in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))
XY.sort()
for i in range(n - 2):
    xi, yi = XY[i]
    for j in range(i + 1, n - 1):
        xj, yj = XY[j]
        for k in range(j + 1, n):
            xk, yk = XY[k]
            if (xj - xi) * (yk - yi) == (yj - yi) * (xk - xi):
                print("Yes")
                exit()
print("No")
