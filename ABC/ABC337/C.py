n = int(input())
(*a,) = map(int, input().split())
m = {}
now = None
for i in range(n):
    if a[i] == -1:
        now = i + 1
    else:
        m[a[i]] = i + 1
lst = []
while now in m:
    lst.append(now)
    now = m[now]
lst.append(now)
print(*lst)
