n = [int(i) for i in list(input())]
a, b = 0, 1
for i in n:
    a, b = min(a+i, b+10-i), min(a+(i+1), b+10-(i+1))
print(a)
