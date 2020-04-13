n = int(input())
s = sum([int(i) for i in list(str(n))])
if n % s == 0:
    print('Yes')
else:
    print('No')
