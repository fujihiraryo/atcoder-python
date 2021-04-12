n = int(input())
d, c, s = [], [], []
for _ in range(n):
    di, ci, si = map(int, input().split())
    d.append(di)
    c.append(ci)
    s.append(si)
idx = list(range(n))
idx.sort(key=lambda i: d[i])


def check(bit):
    day = 0
    for i in idx:
        if (1 << i) & bit:
            day += c[i]
            if day > d[i]:
                return False
    return True


ans = 0
for bit in range(1 << n):
    if check(bit):
        ans = max(ans, sum(s[i] for i in range(n) if (1 << i) & bit))
print(ans)
