f = lambda x: int(x) - 1
n = int(input())
*a, = map(f, input().split())
*b, = map(f, input().split())
*c, = map(f, input().split())
cnt = [0] * n
for i in range(n):
    cnt[a[i]] += 1
ans = 0
for j in range(n):
    ans += cnt[b[c[j]]]
print(ans)
