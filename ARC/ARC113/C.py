from collections import defaultdict

s = input()
n = len(s)
ss = "$" + s + "$"
c = None
end = [0] * n
for i in range(1, n + 1):
    if c != ss[i] and ss[i - 1] == ss[i] and ss[i] != ss[i + 1]:
        end[i - 1] = 1
        c = ss[i]

d = defaultdict(int)
ans = 0
cnt = 0
for i in range(1, n)[::-1]:
    if end[i]:
        ans += cnt - d[s[i]]
        d.clear()
    cnt += 1
    d[s[i]] += 1
print(ans)
