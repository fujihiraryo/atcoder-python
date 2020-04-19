a, b = map(int, input().split())
x = int(str(a)+str(b))
for i in range(10000):
    if i**2 == x:
        print('Yes')
        exit()
print('No')
