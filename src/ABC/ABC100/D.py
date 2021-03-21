from itertools import product

n, m = map(int, input().split())
x, y, z = [], [], []
for _ in range(n):
    xi, yi, zi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)
ans = 0
for sx, sy, sz in product([1, -1], repeat=3):
    ans = max(
        ans,
        sum(sorted([sx * x[i] + sy * y[i] + sz * z[i] for i in range(n)])[::-1][:m]),
    )
print(ans)
