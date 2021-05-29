from bisect import bisect_left
from itertools import permutations

n, m = map(int, input().split())
*w, = map(int, input().split())
vl = []
for _ in range(m):
    li, vi = map(int, input().split())
    vl.append((vi, li))

vl.sort()
ml = 0
v, l = [-1], [0]
for i in range(m):
    vi, li = vl[i]
    ml = max(ml, li)
    v.append(vi)
    l.append(ml)

if max(w) > v[1]:
    print(-1)
    exit()

ans = 10 ** 20
for perm in permutations(range(n)):
    dist = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = sum(w[k] for k in perm[i : j + 1])
            dist[i][j] = l[bisect_left(v, x) - 1]
    dp = [0] * n
    for j in range(1, n):
        for i in range(j):
            dp[j] = max(dp[j], dp[i] + dist[i][j])
    ans = min(ans, dp[n - 1])
print(ans)
