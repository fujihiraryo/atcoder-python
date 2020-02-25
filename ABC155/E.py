N = [int(_) for _ in list(input())]
a, b = 0, 1
for n in N:
    a, b = min(a+n, b+10-n), min(a+(n+1), b+10-(n+1))
print(a)
