def f(n):
    if n == 0 or n == 1:
        return n
    m, k = n // 10, n % 10
    return min(f(m) + k, f(m + 1) + 10 - k)


print(f(91))
