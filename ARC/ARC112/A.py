def ans(x, y):
    if y < 2 * x:
        return 0
    return (y - 2 * x + 2) * (y - 2 * x + 1) // 2


for _ in range(int(input())):
    x, y = map(int, input().split())
    print(ans(x, y))
