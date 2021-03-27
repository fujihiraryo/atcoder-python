h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]
cnt = 0
i, j = x - 1, y - 1
while i > 0 and s[i - 1][j] == ".":
    i -= 1
    cnt += 1
i, j = x - 1, y - 1
while i < h - 1 and s[i + 1][j] == ".":
    i += 1
    cnt += 1
i, j = x - 1, y - 1
while j > 0 and s[i][j - 1] == ".":
    j -= 1
    cnt += 1
i, j = x - 1, y - 1
while j < w - 1 and s[i][j + 1] == ".":
    j += 1
    cnt += 1
print(cnt + 1)
