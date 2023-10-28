n = int(input())
for x in range(n, 919 + 1):
    a = (x // 100) % 10
    b = (x // 10) % 10
    c = x % 10
    if a * b == c:
        print(x)
        exit()
