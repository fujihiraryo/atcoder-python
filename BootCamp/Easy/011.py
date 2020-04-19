n = int(input())
# n = 100
m = 0
x = 1
for i in range(1, n+1):
    a = i
    c = 0
    while a % 2 == 0:
        a = a//2
        c += 1
    if c > m:
        x = i
    m = max(m, c)
print(x)
