from collections import Counter

n = int(input())
*a, = map(int, input().split())
sgn = (1, -1)
b = [a[i] * sgn[i % 2] for i in range(n)]
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + b[i]
c = Counter(s)
ans = 0
for x in c:
    ans += c[x] * (c[x] - 1) // 2
print(ans)
