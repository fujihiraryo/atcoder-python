*a, = map(int, input().split())
a = list(a)
a.sort()
if a[0] - a[1] == a[1] - a[2]:
    print("Yes")
else:
    print("No")
