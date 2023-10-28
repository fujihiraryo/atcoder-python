n = int(input())
lst = []
for _ in range(n):
    t, d = map(int, input().split())
    lst.append((t, d))
lst.sort(key=lambda x: (x[0] + x[1], x[0]))
ans = 1
now = lst[0][0] + 1
for t, d in lst[1:]:
    if now < t:
        now = t
    if now <= t + d:
        ans += 1
        now += 1
print(ans)
