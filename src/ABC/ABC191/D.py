x, y, r = map(float, input().split())
d = 10 ** 4
x = int(f"{x:.4f}".replace(".", ""))
y = int(f"{y:.4f}".replace(".", ""))
r = int(f"{r:.4f}".replace(".", ""))
ans = 0
for i in range(-2 * (10 ** 5), 2 * 10 ** 5 + 1):
    k = i * d
    if r < abs(k - x):
        continue
    s = r ** 2 - (k - x) ** 2
    a, b = 0, r + 1
    while b - a > 1:
        c = (a + b) // 2
        if c ** 2 <= s:
            a = c
        else:
            b = c
    ans += (y + a) // d + (a - y) // d + 1
print(ans)
