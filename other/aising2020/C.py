n = int(input())
f = {}
for x in range(1, n + 1):
    for y in range(1, int(max((n - x ** 2), 0) ** 0.5) + 2):
        for z in range(1, int(max((n - x ** 2 - y ** 2), 0) ** 0.5) + 2):
            a = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            try:
                f[a] += 1
            except BaseException:
                f[a] = 1
for i in range(1, n + 1):
    try:
        print(f[i])
    except BaseException:
        print(0)
