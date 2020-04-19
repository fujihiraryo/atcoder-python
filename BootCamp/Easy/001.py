a, b = map(int, input().split())
x = 1
c = 0
while x < b:
    c += 1
    x += a-1
print(c)
