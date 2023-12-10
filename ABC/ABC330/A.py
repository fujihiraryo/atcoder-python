n, l = map(int, input().split())
(*a,) = map(int, input().split())
ans = 0
for i in range(n):
    if a[i] >= l:
        ans += 1
print(ans)
