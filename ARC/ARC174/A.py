INF = 10**30
n, c = map(int, input().split())
(*a,) = map(int, input().split())
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]

mins = [INF] * (n + 2)
for i in range(n + 1):
    mins[i + 1] = min(mins[i], s[i])

maxs = [-INF] * (n + 2)
for i in range(n + 1):
    maxs[i + 1] = max(maxs[i], s[i])

if c > 0:
    max_diff = -INF
    for i in range(1, n + 1):
        max_diff = max(max_diff, s[i] - mins[i])
    print(max(s[n], s[n] + (c - 1) * max_diff))
else:
    min_diff = INF
    for i in range(1, n + 1):
        min_diff = min(min_diff, s[i] - maxs[i])
    print(max(s[n], s[n] + (c - 1) * min_diff))
