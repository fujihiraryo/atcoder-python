n, m = map(int, input().split())
cnt = 0
tmp = 0
lst = [tuple(map(int, input().split())) for _ in range(m)]
lst.sort(key=lambda x: x[1])
for a, b in lst:
    if tmp < a:
        tmp = b - 1
        cnt += 1
print(cnt)
