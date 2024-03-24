mod = 998244353
n = int(input())
(*p,) = map(int, input().split())
p = [p[i] - 1 for i in range(n)]
s = input()
# 最終的に左回りになる
left = 1
visited = [False] * n
for x in p:
    visited[x] = True
    if visited[(x + 1) % n]:
        if s[x] == "?":
            left = (left * 2) % mod
    else:
        if s[x] == "R":
            left = 0
            break
# 最終的に右回りになる
right = 1
visited = [False] * n
for x in p:
    visited[x] = True
    if visited[(x - 1) % n]:
        if s[x] == "?":
            right = (right * 2) % mod
    else:
        if s[x] == "L":
            right = 0
            break
print((left + right) % mod)
