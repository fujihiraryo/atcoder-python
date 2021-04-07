n = int(input())
lst = [input().split() for _ in range(n)]
x = input()
ans = 0
flag = 0
for s, t in lst:
    if flag:
        ans += int(t)
    if s == x:
        flag = 1
print(ans)
