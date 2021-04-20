import bisect

INF = 1 << 64
n = int(input())
(*a,) = map(int, input().split())
a.sort()
a.append(INF)
for _ in range(int(input())):
    b = int(input())
    i = bisect.bisect_left(a, b)
    x = abs(a[i - 1] - b)
    y = abs(a[i] - b)
    print(min(x, y))
