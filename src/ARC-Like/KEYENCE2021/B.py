n, k = map(int, input().split())
(*a,) = map(int, input().split())
c = [0] * n
for i in range(n):
    c[a[i]] += 1
ans = 0
tmp = k
for j in range(n):
    ans += min(c[j], tmp)
    tmp = min(tmp, c[j])
print(ans)
