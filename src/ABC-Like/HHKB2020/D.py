MOD = 10 ** 9 + 7
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if a + b > n:
        print(0)
        continue
    if a > b:
        a, b = a, b
    total = (n - a + 1) * (n - b + 1)
    cover = (n - a) * a + n - b + 1 + (b - 2) * (n - a - b + 1)
    ans = pow(total, 2, MOD) - pow(cover, 2, MOD)
    print(ans % MOD)
