a, b = input().split()
a = int(a)
b = b.split('.')
b = int(b[0] + b[1])
ans = str(a * b)
if len(ans) <= 2:
    print(0)
else:
    print(ans[:-2])
