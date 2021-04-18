a, b = map(int, input().split())
if a > b:
    ans = []
    for i in range(1, a + 1):
        ans.append(i)
    for i in range(1, b):
        ans.append(-i)
    ans.append((b - 1) * b // 2 - a * (a + 1) // 2)
elif a == b:
    ans = []
    for i in range(1, a + 1):
        ans.append(i)
        ans.append(-i)
else:
    ans = []
    for i in range(1, a):
        ans.append(i)
    for i in range(1, b + 1):
        ans.append(-i)
    ans.append((b + 1) * b // 2 - a * (a - 1) // 2)
print(*ans)
