n, a, b = map(int, input().split())
c = b - a
if c % 2:
    print(min(a - 1, n - b) - (-c // 2))
else:
    print(-(-c // 2))
