n = int(input())
d, c, s = [], [], []
for _ in range(n):
    di, ci, si = map(int, input().split())
    d.append(di)
    c.append(ci)
    s.append(si)
m = max(d)
dp = [0] * (m + 1)
for i in sorted(range(n), key=lambda i: d[i]):
    new = dp[:]
    for j in range(m + 1):
        if j + c[i] > d[i]:
            continue
        new[j + c[i]] = max(new[j + c[i]], dp[j] + s[i])
    dp = new
print(max(dp))
