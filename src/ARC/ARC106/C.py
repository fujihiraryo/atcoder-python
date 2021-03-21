n, m = map(int, input().split())
if n == 1 and m == 0:
    print(1, 2)
    exit()
if m < 0 or n - 2 < m:
    print(-1)
    exit()
x = 1
for _ in range(n - m - 1):
    print(x, 10 ** 9 - x)
    x += 1
for i in range(m + 1):
    print(x, x + 1)
    x += 2
