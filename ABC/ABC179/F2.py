n, q = map(int, input().split())
n -= 2
row = [n] * n
col = [n] * n
ans = n * n
for _ in range(q):
    t, x = map(int, input().split())
    x -= 2
    if t == 1:
        for i in range(x, col[0]):
            row[i] = row[0]
        col[0] = min(col[0], x)
        ans -= row[x]
    else:
        for i in range(x, row[0]):
            col[i] = col[0]
        row[0] = min(row[0], x)
        ans -= col[x]
print(ans)
