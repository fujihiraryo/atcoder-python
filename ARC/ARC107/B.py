def f(n, x):
    # 1<=a,b<=n and a+b=x
    if x < 2 or 2 * n < x:
        return 0
    return abs(x - 2 * min(x - 1, n)) + 1


n, k = map(int, input().split())
print(sum(f(n, x) * f(n, x + k) for x in range(2, 2 * n - k + 1)))
