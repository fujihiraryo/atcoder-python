n = int(input())
(*a,) = map(int, input().split())
a.sort(reverse=True)
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
print(a, s)
ans = 0
for i in range(n - 1):
    ans += (n - i - 1) * a[i] - s[n] + s[i + 1]
print(ans)
