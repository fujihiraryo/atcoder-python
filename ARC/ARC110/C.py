n = int(input())
(*lst,) = map(lambda x: int(x) - 1, input().split())
ans = []
cur = 0
for i in range(n):
    if lst[i] == cur:
        for j in range(cur, i)[::-1]:
            ans.append(j)
        cur = i
for i in ans:
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
if len(ans) == n - 1 and lst == list(range(n)):
    print(*map(lambda x: x + 1, ans), sep="\n")
else:
    print(-1)
