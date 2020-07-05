n = int(input())
ans = sum([(i + 1) * (n - i) for i in range(n)])
for i in range(n - 1):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    ans -= x * (n + 1 - y)
print(ans)
