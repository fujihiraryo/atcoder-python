a = input()
b = input()
m, n = len(a), len(b)
if m < n:
    print("LESS")
    exit()
elif m > n:
    print("GREATER")
    exit()
else:
    for i in range(n):
        if int(a[i]) > int(b[i]):
            print("GREATER")
            exit()
        if int(a[i]) < int(b[i]):
            print("LESS")
            exit()
print("EQUAL")
