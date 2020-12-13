L = int(input())
a, b = 1, 1
for i in range(11):
    a *= L - 1 - i
    b *= 11 - i
print(a // b)
