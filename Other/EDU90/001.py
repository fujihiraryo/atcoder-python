n, l = map(int, input().split())
k = int(input())
(*a,) = map(int, input().split())
b = [a[0]]
for i in range(1, n):
    b.append(a[i] - a[i - 1])
b.append(l - a[-1])


def judge(x):
    cnt = 0
    tmp = 0
    for i in range(n + 1):
        tmp += b[i]
        if tmp >= x:
            cnt += 1
            tmp = 0
    return cnt >= k + 1


x, y = 0, l
while y - x > 1:
    z = (x + y) // 2
    if judge(z):
        x = z
    else:
        y = z
print(x)
