s = input()
cnt = {}
for x in s:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1
lst = []
for x in cnt:
    lst.append((-cnt[x], x))
lst.sort()
print(lst[0][1])
