m, k = map(int, input().split())
if k >= 2 ** m or (m == 1 and k == 1):
    print(-1)
    exit()
if k == 0:
    a = []
    for i in range(2 ** m):
        a.append(i)
        a.append(i)
    print(*a)
    exit()
b = [i for i in range(1, 2 ** m) if i != k]
a = [0, k, 0] + b + [k] + b[::-1]
print(*a)
