n, m = map(int, input().split())
s = list(input())
t = list(input())
lst = [i for i in range(n - m + 1)]
for i in lst:
    res = True
    if s[i : i + m] == ["#"] * m:
        continue
    for x, y in zip(s[i : i + m], t):
        if x != "#" and x != y:
            res = False
    if res:
        s[i : i + m] = "#" * m
        for j in range(max(0, i - (m - 1)), i):
            if j + m <= n:
                lst.append(j)
        for j in range(i + 1, min(i + m, n)):
            if j + m <= n:
                lst.append(j)
if s == ["#"] * n:
    print("Yes")
else:
    print("No")
