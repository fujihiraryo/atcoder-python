n, m, k = map(int, input().split())
(*a,) = map(int, input().split())
a = set(a)
x_list, y_list = [0], [0]
x_sum, y_sum = 0, 0
for i in range(1, n + 1):
    if n - i in a:
        x, y = 1, 0
    else:
        x, y = x_sum / m, 1 + y_sum / m
    x_list.append(x)
    y_list.append(y)
    x_sum += x
    y_sum += y
    if i >= m:
        x_sum -= x_list[i - m]
        y_sum -= y_list[i - m]
x, y = x_list[-1], y_list[-1]
if x >= 1 - 10 ** (-7):
    print(-1)
    exit()
print(y / (1 - x))
