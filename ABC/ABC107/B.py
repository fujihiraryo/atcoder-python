h, w = map(int, input().split())
a = [input() for _ in range(h)]
h_lst, w_lst = [], []
for i in range(h):
    if all(a[i][j] == "." for j in range(w)):
        h_lst.append(i)
for j in range(w):
    if all(a[i][j] == "." for i in range(h)):
        w_lst.append(j)
b = []
for i in range(h):
    if i in h_lst:
        continue
    bi = ""
    for j in range(w):
        if j in w_lst:
            continue
        bi += a[i][j]
    b.append(bi)
print(*b, sep="\n")
