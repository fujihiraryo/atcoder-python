a, b = map(int, input().split())
n = 100
print(n, n)
s = [[0] * n for _ in range(n)]
for i in range(n // 2):
    for j in range(n):
        s[i][j] = 1
for i in range(0, n // 2, 2):
    for j in range(0, n, 2):
        if a > 1:
            s[i][j] = 0
            a -= 1
for i in range(n // 2 + 1, n, 2):
    for j in range(0, n, 2):
        if b > 1:
            s[i][j] = 1
            b -= 1
for i in range(n):
    x = ""
    for j in range(n):
        x += (".", "#")[s[i][j]]
    print(x)
