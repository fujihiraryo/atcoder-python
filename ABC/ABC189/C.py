n = int(input())
(*a,) = map(int, input().split())
ans = 0
for i in range(n):
    x = a[i]
    for j in range(i, n):
        x = min(x, a[j])
        ans = max(ans, x * (j - i + 1))
print(ans)
