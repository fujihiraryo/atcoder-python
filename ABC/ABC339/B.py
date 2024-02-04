h, w, n = map(int, input().split())
grid = [["."] * w for _ in range(h)]
i, j = 0, 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
k = 0
for _ in range(n):
    if grid[i][j] == ".":
        grid[i][j] = "#"
        k = (k + 1) % 4
    else:
        grid[i][j] = "."
        k = (k - 1) % 4
    i = (i + dirs[k][0]) % h
    j = (j + dirs[k][1]) % w
for i in range(h):
    print("".join(grid[i]))
