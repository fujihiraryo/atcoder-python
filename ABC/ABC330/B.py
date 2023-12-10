n, l, r = map(int, input().split())
(*a,) = map(int, input().split())
ans = []
for i in range(n):
    if l <= a[i] <= r:
        ans.append(a[i])
    elif a[i] < l:
        ans.append(l)
    else:
        ans.append(r)
print(*ans)
