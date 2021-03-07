n, m, q = map(int, input().split())
table = [[0] * (n + 2) for _ in range(n + 2)]
for _ in range(m):
    li, ri = map(int, input().split())
    table[1][ri] += 1
    table[1][n + 1] -= 1
    table[li + 1][ri] -= 1
    table[li + 1][n + 1] += 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        table[i][j] += table[i - 1][j]
for j in range(1, n + 1):
    for i in range(1, n + 1):
        table[i][j] += table[i][j - 1]
for _ in range(q):
    i, j = map(int, input().split())
    print(table[i][j])
