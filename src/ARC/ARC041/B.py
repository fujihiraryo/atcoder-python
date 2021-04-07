n, m = map(int, input().split())
b = [[int(x) for x in input()] for _ in range(n)]
a = [[0] * m for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, m - 1):
        a[i][j] = b[i - 1][j]
        b[i][j - 1] -= a[i][j]
        b[i][j + 1] -= a[i][j]
        b[i - 1][j] -= a[i][j]
        b[i + 1][j] -= a[i][j]
for i in range(n):
    print("".join(map(str, a[i])))
