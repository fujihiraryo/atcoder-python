n, k = map(int, input().split())
(*A,) = map(int, input().split())
i, j = 0, 10 ** 9
while j - i > 1:
    c = (i + j) // 2
    if sum(-(-a // c) - 1 for a in A) <= k:
        j = c
    else:
        i = c
print(j)
