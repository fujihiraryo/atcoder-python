x, y, a, b = map(int, input().split())
cnt = 0
while x * a < min(x + b, y):
    x *= a
    cnt += 1
cnt += (y - x - 1) // b
print(cnt)
