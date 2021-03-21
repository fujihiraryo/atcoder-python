n, k = map(int, input().split())
lst = []
for _ in range(n):
    a, b, c = map(int, input().split())
    lst.append((a, c))
    lst.append((b + 1, -c))
lst.sort()
s, x, ans = 0, 0, 0
for y, c in lst:
    ans += min(k, s) * (y - x)
    s += c
    x = y
print(ans)
