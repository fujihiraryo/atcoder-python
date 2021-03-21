import bisect

n = int(input())
(*L,) = map(int, input().split())
L.sort()
cnt = 0
for i in range(n - 2):
    a = L[i]
    for j in range(i + 1, n - 1):
        b = L[j]
        l = max(j + 1, bisect.bisect_left(L, b - a))
        r = bisect.bisect_left(L, b + a)
        cnt += r - l
print(cnt)
