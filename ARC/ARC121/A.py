n = int(input())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
x_idx = list(range(n))
y_idx = list(range(n))
x_idx.sort(key=lambda i: x[i])
y_idx.sort(key=lambda i: y[i])
if {x_idx[0], x_idx[n - 1]} == {y_idx[0], y_idx[n - 1]}:
    ans = max(
        x[x_idx[-2]] - x[x_idx[0]],
        x[x_idx[n - 1]] - x[x_idx[1]],
        y[y_idx[-2]] - y[y_idx[0]],
        y[y_idx[n - 1]] - y[y_idx[1]],
    )
elif x[x_idx[n - 1]] - x[x_idx[0]] >= y[y_idx[n - 1]] - y[y_idx[0]]:
    ans = max(
        x[x_idx[-2]] - x[x_idx[0]],
        x[x_idx[n - 1]] - x[x_idx[1]],
        y[y_idx[n - 1]] - y[y_idx[0]],
    )
else:
    ans = max(
        x[x_idx[n - 1]] - x[x_idx[0]],
        y[y_idx[-2]] - y[y_idx[0]],
        y[y_idx[n - 1]] - y[y_idx[1]],
    )
print(ans)
