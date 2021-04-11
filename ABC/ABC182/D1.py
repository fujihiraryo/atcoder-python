n = int(input())
*a, = map(int, input().split())
# s[i]=sum(a[:i])
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
# t[i]=max(s[:i])
t = [0] * (n + 2)
for i in range(n + 1):
    t[i + 1] = max(s[i], t[i])
ans = 0
x = 0
for i in range(n):
    ans = max(ans, x + t[i + 2])
    x += s[i + 1]
print(ans)
