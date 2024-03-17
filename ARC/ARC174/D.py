def tle(n):
    ans = 0
    for x in range(1, n + 1):
        y = int(x**0.5)
        if str(x)[: len(str(y))] == str(y):
            ans += 1
    return ans


def solve(n):
    ans = 1
    i = 0
    while True:
        x = int("9" * i + "8" + "0" * (i + 1))
        if n < x:
            break
        i += 1
        ans += 1
    i = 1
    while True:
        x = int("9" * i + "0" * i)
        y = int("9" * (2 * i))
        if n < x:
            break
        if x <= n <= y:
            ans += n - x + 1
            break
        ans += y - x + 1
        i += 1
    i = 1
    while True:
        x = int("1" + "0" * (2 * i))
        y = int("1" + "0" * i + "9" * i)
        if n < x:
            break
        if x <= n <= y:
            ans += n - x + 1
            break
        ans += y - x + 1
        i += 1
    return ans


for _ in range(int(input())):
    print(solve(int(input())))
