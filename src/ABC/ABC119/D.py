import bisect

a, b, q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
for _ in range(q):
    x = int(input())
    ans = 10 ** 20
    i1 = bisect.bisect_left(s, x)
    i0 = max(0, i1 - 1)
    if i0 >= 0:
        j1 = bisect.bisect_left(t, s[i0])
        j0 = max(0, j1 - 1)
        ans = min(ans, abs(x - s[i0]) + abs(s[i0] - t[j0]))
        if j1 < b:
            ans = min(ans, abs(x - s[i0]) + abs(s[i0] - t[j1]))
    if i1 < a:
        j1 = bisect.bisect_left(t, s[i1])
        j0 = max(0, j1 - 1)
        ans = min(ans, abs(x - s[i1]) + abs(s[i1] - t[j0]))
        if j1 < b:
            ans = min(ans, abs(x - s[i1]) + abs(s[i1] - t[j1]))
    j1 = bisect.bisect_left(t, x)
    j0 = max(0, j1 - 1)
    if j0 >= 0:
        i1 = bisect.bisect_left(s, t[j0])
        i0 = max(0, i1 - 1)
        if i0 >= 0:
            ans = min(ans, abs(x - t[j0]) + abs(t[j0] - s[i0]))
        if i1 < a:
            ans = min(ans, abs(x - t[j0]) + abs(t[j0] - s[i1]))
    if j1 < b:
        i1 = bisect.bisect_left(s, t[j1])
        i0 = max(0, i1 - 1)
        if i0 >= 0:
            ans = min(ans, abs(x - t[j1]) + abs(t[j1] - s[i0]))
        if i1 < a:
            ans = min(ans, abs(x - t[j1]) + abs(t[j1] - s[i1]))
    print(ans)
