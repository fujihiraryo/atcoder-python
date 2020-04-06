s, l, r = map(int, input().split())
if l <= s <= r:
    print(s)
elif s < l:
    print(l)
elif r < s:
    print(r)
