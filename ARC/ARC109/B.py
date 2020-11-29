n = int(input())
a, b = 0, 10 ** 18
while b - a > 1:
    c = (a + b) // 2
    if c * (c + 1) // 2 <= n + 1:
        a = c
    else:
        b = c
print(n + 1 - a)
