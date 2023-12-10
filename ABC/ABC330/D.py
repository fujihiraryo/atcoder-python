n = int(input())
s = [input() for _ in range(n)]
row = [0] * n
col = [0] * n
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            row[i] += 1
            col[j] += 1
ans = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            ans += (row[i] - 1) * (col[j] - 1)
print(ans)
