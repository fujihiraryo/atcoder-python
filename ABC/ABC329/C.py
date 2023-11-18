from collections import defaultdict

n = int(input())
s = input()
cnt = defaultdict(int)
last = s[0]
x = 0
for c in s[1:]:
    if c != last:
        cnt[last] = max(cnt[last], x + 1)
        last = c
        x = 0
    else:
        x += 1
cnt[last] = max(cnt[last], x + 1)
ans = 0
for c in cnt.keys():
    ans += cnt[c]
print(ans)
