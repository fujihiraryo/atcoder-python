def light_up(array):
    size = len(array)
    tmp = None
    for i in range(size):
        if array[i] is None and tmp == 0:
            array[i] = 0
        if array[i] == 0:
            tmp = 0
        if array[i] == 1:
            tmp = 1
    tmp = None
    for i in range(size - 1, -1, -1):
        if array[i] is None and tmp == 0:
            array[i] = 0
        if array[i] == 0:
            tmp = 0
        if array[i] == 1:
            tmp = 1


h, w, n, m = map(int, input().split())
raw = [[None] * w for _ in range(h)]
col = [[None] * h for _ in range(w)]
for _ in range(n):
    a, b = map(int, input().split())
    raw[a - 1][b - 1] = 0
    col[b - 1][a - 1] = 0
for _ in range(m):
    a, b = map(int, input().split())
    raw[a - 1][b - 1] = 1
    col[b - 1][a - 1] = 1
for i in range(h):
    light_up(raw[i])
for j in range(w):
    light_up(col[j])
cnt = 0
for i in range(h):
    for j in range(w):
        if raw[i][j] == 0 or col[j][i] == 0:
            cnt += 1
print(cnt)
