from collections import defaultdict

n, m = map(int, input().split())
(*a,) = map(int, input().split())
a = [a[i] % m for i in range(n)]
s = [0]
for i in range(n):
    s.append((s[i] + a[i]) % m)
c = defaultdict(int)
for x in s:
    c[x] += 1
ans = 0
for x in c:
    ans += c[x] * (c[x] - 1) // 2
print(ans)
