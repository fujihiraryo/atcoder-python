from collections import defaultdict

n, k = map(int, input().split())
(*a,) = map(int, input().split())
s = [0]
for i in range(n):
    s.append(s[-1] + a[i])
s = [(s[i] - i) % k for i in range(n + 1)]
c = defaultdict(int)
for i in range(min(k, n + 1)):
    c[s[i]] += 1
ans = 0
for i in range(n):
    c[s[i]] -= 1
    ans += c[s[i]]
    if i + k < n + 1:
        c[s[i + k]] += 1
print(ans)
