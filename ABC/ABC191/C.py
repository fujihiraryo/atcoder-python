h, w = map(int, input().split())
s = [input() for _ in range(h)]
cnt = 0
for i in range(1, h):
    for j in range(1, w):
        lst = [s[i - 1][j - 1], s[i - 1][j], s[i][j - 1], s[i][j]]
        white = lst.count("#")
        black = lst.count(".")
        if white == 1 and black == 3:
            cnt += 1
        if white == 3 and black == 1:
            cnt += 1
print(cnt)
