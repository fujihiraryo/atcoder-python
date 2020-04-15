S = list(input())
a, b = 0, 0
for s in S:
    if s == '1':
        a += 1
    if s == '0':
        b += 1
print(min(a, b)*2)
