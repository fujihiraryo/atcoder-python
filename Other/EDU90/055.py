n, p, q = map(int, input().split())
(*a,) = map(int, input().split())
ans = 0
for i0 in range(n - 4):
    x0 = a[i0] % p
    for i1 in range(i0 + 1, n - 3):
        x1 = x0 * a[i1] % p
        for i2 in range(i1 + 1, n - 2):
            x2 = x1 * a[i2] % p
            for i3 in range(i2 + 1, n - 1):
                x3 = x2 * a[i3] % p
                for i4 in range(i3 + 1, n):
                    x4 = x3 * a[i4] % p
                    if x4 == q:
                        ans += 1
print(ans)
