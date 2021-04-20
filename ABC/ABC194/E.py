n, m = map(int, input().split())
(*a,) = map(int, input().split())
idx = [[-1] for x in range(max(a) + 1)]
for i in range(n):
    idx[a[i]].append(i)
for lst in idx:
    lst.append(n)
for x, lst in enumerate(idx):
    k = len(lst)
    for i in range(k - 1):
        if lst[i + 1] - lst[i] - 1 >= m:
            print(x)
            exit()
print(x + 1)
