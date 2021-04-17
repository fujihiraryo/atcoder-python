n, m = map(int, input().split())
*a, = map(int, input().split())
*b, = map(int, input().split())
a = set(a)
b = set(b)
ans = []
for i in range(1, 1000 + 1):
    if i in a and i not in b:
        ans.append(i)
    elif i not in a and i in b:
        ans.append(i)
print(*ans)
