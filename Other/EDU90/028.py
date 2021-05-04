MAX = 1001
board = [[0] * MAX for _ in range(MAX)]
n = int(input())
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    board[lx][ly] += 1
    board[rx][ly] -= 1
    board[lx][ry] -= 1
    board[rx][ry] += 1
for x in range(MAX):
    for y in range(1, MAX):
        board[x][y] += board[x][y - 1]
for y in range(MAX):
    for x in range(1, MAX):
        board[x][y] += board[x - 1][y]
ans = [0] * (n + 1)
for x in range(MAX):
    for y in range(MAX):
        ans[board[x][y]] += 1
print(*ans[1:], sep="\n")
