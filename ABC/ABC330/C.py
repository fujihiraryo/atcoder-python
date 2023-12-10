d = int(input())
ans = 10**20
y = 0
while y**2 <= d:
    x = int((d - y**2) ** 0.5)
    ans = min(ans, abs(x**2 + y**2 - d))
    ans = min(ans, abs((x + 1) ** 2 + y**2 - d))
    y += 1
print(ans)
