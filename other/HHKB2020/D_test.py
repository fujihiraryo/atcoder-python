MOD = 10 ** 9 + 7
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if a > b:
        a, b = a, b
    total = (n - a + 1) * (n - b + 1)
    cover = 0
    for i in range(n - b + 1):
        cover += min(n - a, i + b - 1) - max(0, i - a + 1) + 1
    ans = pow(total, 2, MOD) - pow(cover, 2, MOD)
    print(ans % MOD)
