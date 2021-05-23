MOD = 998244353
h, w = map(int, input().split())
s = [input() for _ in range(h)]
lst = [set() for _ in range(h + w)]
for i in range(h):
    for j in range(w):
        lst[i + j].add(s[i][j])
ans = 1
for k in range(h + w - 1):
    if "R" in lst[k] and "B" in lst[k]:
        ans = 0
    elif len(lst[k]) == 1 and "." in lst[k]:
        ans *= 2
        ans %= MOD
print(ans)
