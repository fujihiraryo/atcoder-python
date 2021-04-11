n, k = map(int, input().split())
(*x,) = map(int, input().split())
a = [0] + [-x[i] for i in range(n) if x[i] < 0][::-1]
b = [0] + [x[i] for i in range(n) if x[i] >= 0]
na, nb = len(a) - 1, len(b) - 1
ans = 1 << 30
for i in range(max(0, k - nb), min(k, na) + 1):
    ans = min(ans, 2 * a[i] + b[k - i], a[i] + 2 * b[k - i])
print(ans)
