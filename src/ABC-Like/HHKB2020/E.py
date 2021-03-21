MOD = int(1e9 + 7)
h, w = map(int, input().split())
s = [input() for _ in range(h)]
c = [[0] * w for _ in range(h)]
for i in range(h):
    cnt = 0
    for j in range(w):
        if s[i][j] == "#":
            cnt = 0
        c[i][j] += cnt
        if s[i][j] == ".":
            cnt += 1
for i in range(h):
    cnt = 0
    for j in range(w)[::-1]:
        if s[i][j] == "#":
            cnt = 0
        c[i][j] += cnt
        if s[i][j] == ".":
            cnt += 1
for j in range(w):
    cnt = 0
    for i in range(h):
        if s[i][j] == "#":
            cnt = 0
        c[i][j] += cnt
        if s[i][j] == ".":
            cnt += 1
for j in range(w):
    cnt = 0
    for i in range(h)[::-1]:
        if s[i][j] == "#":
            cnt = 0
        c[i][j] += cnt
        if s[i][j] == ".":
            cnt += 1
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            c[i][j] += 1
k = sum(s[i][j] == "." for i in range(h) for j in range(w))
table = []
tmp = 1
for _ in range(k + 1):
    table.append(tmp)
    tmp = (tmp * 2) % MOD
ans = 0
for i in range(h):
    for j in range(w):
        ans += (table[k] - table[k - c[i][j]]) % MOD
        ans %= MOD
print(ans)
