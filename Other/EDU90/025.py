from itertools import product

n, b = map(int, input().split())
ans = 0
if b <= n and str(b).count("0") > 0:
    ans += 1
for p2, p3, p5, p7 in product(range(20), repeat=4):
    x = pow(2, p2) * pow(3, p3) * pow(5, p5) * pow(7, p7)
    y = 1
    for i in map(int, str(x + b)):
        y *= i
    if x + b <= n and x == y:
        ans += 1
print(ans)
