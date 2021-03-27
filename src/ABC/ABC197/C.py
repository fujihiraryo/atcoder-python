def calc(s):
    global n
    global a
    tmp = 0
    total = 0
    for i in range(n):
        tmp |= a[i]
        if (1 << i) & s:
            total ^= tmp
            tmp = 0
    return total ^ tmp


n = int(input())
*a, = map(int, input().split())
ans = 1 << 60
for s in range(1 << (n - 1)):
    ans = min(ans, calc(s))
print(ans)
