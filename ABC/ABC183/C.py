import itertools

n, k = map(int, input().split())
T = [list(map(int, input().split())) for i in range(n)]
A = itertools.permutations(range(1, n))
cnt = 0
for lst in A:
    now = 0
    tmp = 0
    for x in lst:
        tmp += T[now][x]
        now = x
    tmp += T[now][0]
    if tmp == k:
        cnt += 1
print(cnt)
