MOD = 10 ** 5
n, k = map(int, input().split())
used = {}
lst = []
x = n
for j in range(MOD + 1):
    if x in used:
        i = used[x]
        break
    used[x] = j
    lst.append(x)
    y = sum(int(c) for c in str(x))
    x = (x + y) % MOD
if k <= i:
    print(lst[k])
else:
    print(lst[i + (k - i) % (j - i)])
