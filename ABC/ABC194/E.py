n, m = map(int, input().split())
(*a,) = map(int, input().split())
idx = [[-1] for x in range(n)]
for i in range(n):
    idx[a[i]].append(i)
for x in range(n):
    idx[x].append(n)
    for i in range(len(idx[x]) - 1):
        if idx[x][i + 1] - idx[x][i] > m:
            print(x)
            exit()
print(n)
