import copy

h, w = map(int, input().split())
a = [[None] * w for _ in range(h)]
b = [[None] * w for _ in range(h)]
for i in range(h):
    (*a[i],) = map(int, input().split())
for i in range(h):
    (*b[i],) = map(int, input().split())

if sorted([sorted(a[i]) for i in range(h)]) != sorted([sorted(b[i]) for i in range(h)]):
    print(-1)
    exit()


# あるリストがaの何行目と一致するか
def find_row(lst):
    for i in range(h):
        if sorted(a[i]) == sorted(lst):
            return i


# あるリストがaの何列目と一致するか
def find_col(lst):
    for j in range(w):
        if sorted([a[i][j] for i in range(h)]) == sorted(lst):
            return j


c = copy.deepcopy(b)

# bの行をソート
for i in range(h):
    for j in range(1, h):
        if find_row(b[j - 1]) > find_row(b[j]):
            b[j - 1], b[j] = b[j], b[j - 1]

# bの列をソート
for i in range(w):
    for j in range(1, w):
        if find_col([b[k][j - 1] for k in range(h)]) > find_col(
            [b[k][j] for k in range(h)]
        ):
            for k in range(h):
                b[k][j - 1], b[k][j] = b[k][j], b[k][j - 1]

if a != b:
    print(-1)
    exit()

row = [find_row(c[i]) for i in range(h)]
col = [find_col([c[i][j] for i in range(h)]) for j in range(w)]

ans = 0

for i in range(h - 1):
    for j in range(i + 1, h):
        if row[i] > row[j]:
            ans += 1

for i in range(w - 1):
    for j in range(i + 1, w):
        if col[i] > col[j]:
            ans += 1

print(ans)
