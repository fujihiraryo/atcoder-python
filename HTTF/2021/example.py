n, m = 20, 100
A = [tuple(map(int, input().split())) for i in range(m)]
ans = ""
x0, y0 = 0, 0
for x, y in A:
    x_dir = "D" if x > x0 else "U"
    y_dir = "R" if y > y0 else "L"
    ans += x_dir * abs(x - x0) + y_dir * abs(y - y0) + "I"
    x0, y0 = x, y
print(ans)
