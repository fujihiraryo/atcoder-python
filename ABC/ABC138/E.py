import bisect

s = [ord(c) - ord("a") for c in input()]
t = [ord(c) - ord("a") for c in input()]
m, n = len(s), len(t)
smap = [[] for _ in range(26)]
for i in range(2 * m):
    smap[s[i % m]].append(i)
sdis = [[None] * m for _ in range(26)]
for i in range(m):
    for k in range(26):
        if smap[k]:
            x = bisect.bisect_left(smap[k], i)
            sdis[k][i] = smap[k][x] - i + 1
i = 0
for j in range(n):
    x = sdis[t[j]][i % m]
    if x is None:
        print(-1)
        exit()
    i += x
print(i)
