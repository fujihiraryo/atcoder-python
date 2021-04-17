n = int(input())
a, b, c = map(int, input().split())
m = 10000
ans = m
for x in range(m):
    for y in range(m):
        if (n - a * x - b * y) % c:
            continue
        z = (n - a * x - b * y) // c
        if z < 0:
            continue
        ans = min(ans, x + y + z)
print(ans)
