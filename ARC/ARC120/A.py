n = int(input())
*a, = map(int, input().split())
s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]
ss = [0] * n
ss[0] = s[0]
for i in range(1, n):
    ss[i] = ss[i - 1] + s[i]
b = [0] * n
b[0] = a[0]
for i in range(1, n):
    b[i] = max(b[i - 1], a[i])
for i in range(n):
    print((i + 1) * b[i] + ss[i])
