n = int(input())
(*a,) = map(int, input().split())
before = {}
after = {}
s = set(a)
for i in range(n - 1):
    after[a[i]] = a[i + 1]
    before[a[i + 1]] = a[i]
for _ in range(int(input())):
    (*q,) = map(int, input().split())
    if q[0] == 1:
        x, y = q[1], q[2]
        s.add(y)
        if x in after:
            z = after[x]
            after[x] = y
            after[y] = z
            before[y] = x
            before[z] = y
        else:
            after[x] = y
            before[y] = x
    else:
        x = q[1]
        s.remove(x)
        if x in before and x in after:
            y = before[x]
            z = after[x]
            before[z] = y
            after[y] = z
            before.pop(x)
            after.pop(x)
        elif x in before:
            y = before[x]
            after.pop(y)
            before.pop(x)
        elif x in after:
            z = after[x]
            before.pop(z)
            after.pop(x)
for x in s:
    break
while x in before:
    x = before[x]
ans = []
while x in after:
    ans.append(x)
    x = after[x]
ans.append(x)
print(*ans)
