a, b = map(int, input().split())
x = a + b
if x >= 15 and b >= 8:
    print(1)
elif x >= 10 and b >= 3:
    print(2)
elif x >= 3:
    print(3)
else:
    print(4)
