n = int(input())
(*a,) = map(int, input().split())
a = [0] + a + [n + 1]
idx = sorted(range(1, n + 1), key=lambda i: a[i])
lhs = [max(0, i - 1) for i in range(n + 2)]
rhs = [min(n + 1, i + 1) for i in range(n + 2)]
ans = 0
for i in idx:
    cnt = (i - lhs[i]) * (rhs[rhs[i]] - rhs[i]) + (rhs[i] - i) * (lhs[i] - lhs[lhs[i]])
    ans += a[i] * cnt
    rhs[lhs[i]], lhs[rhs[i]] = rhs[i], lhs[i]
print(ans)
