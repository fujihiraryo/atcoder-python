from collections import defaultdict

n = int(input())
*a, = map(int, input().split())
a = [a[i] % 200 for i in range(n)]
cnt = defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1
ans = 0
for x in cnt:
    ans += cnt[x] * (cnt[x] - 1) // 2
print(ans)
