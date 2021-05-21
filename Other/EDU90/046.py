n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
*c, = map(int, input().split())
x = [0] * 46
y = [0] * 46
z = [0] * 46
for i in range(n):
    x[a[i] % 46] += 1
    y[b[i] % 46] += 1
    z[c[i] % 46] += 1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += x[i] * y[j] * z[k]
print(ans)
