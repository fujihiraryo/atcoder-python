n = int(input())
a = 2
s = set()
while a ** 2 <= n:
    b = 2
    while pow(a, b) <= n:
        s.add(pow(a, b))
        b += 1
    a += 1
print(n - len(s))
