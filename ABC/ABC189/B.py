n, x = map(int, input().split())
x *= 100
t = 0
for i in range(n):
    v, p = map(int, input().split())
    t += v * p
    if t > x:
        print(i + 1)
        exit()
print(-1)
