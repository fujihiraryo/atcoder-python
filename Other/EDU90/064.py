n, q = map(int, input().split())
(*a,) = map(int, input().split())
b = [a[i + 1] - a[i] for i in range(n - 1)]
ans = sum(abs(b[i]) for i in range(n - 1))
for _ in range(q):
    l, r, v = map(int, input().split())
    i, j = l - 1, r
    # a[i:j]に+v
    if i - 1 >= 0:
        ans += abs(b[i - 1] + v) - abs(b[i - 1])
        b[i - 1] += v
    if j - 1 <= n - 2:
        ans += abs(b[j - 1] - v) - abs(b[j - 1])
        b[j - 1] -= v
    print(ans)
