h, w, m = map(int, input().split())
lst = []
for _ in range(m):
    t, a, x = map(int, input().split())
    lst.append((t, a, x))
lst.reverse()
rows = set(range(1, h + 1))
cols = set(range(1, w + 1))
cnt = [0] * (2 * 10**5 + 1)
for t, a, x in lst:
    if t == 1 and a in rows:
        rows.remove(a)
        cnt[x] += len(cols)
    elif t == 2 and a in cols:
        cols.remove(a)
        cnt[x] += len(rows)
cnt[0] += len(rows) * len(cols)
print(len([x for x in range(2 * 10**5 + 1) if cnt[x] > 0]))
for x in range(2 * 10**5 + 1):
    if cnt[x] > 0:
        print(x, cnt[x])
