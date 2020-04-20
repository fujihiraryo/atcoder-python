d, n = map(int, input().split())
# d, n = 0, 5
# d, n = 1, 11
# d, n = 2, 85
if n != 100:
    print(100**d*n)
else:
    print(100**d*101)
