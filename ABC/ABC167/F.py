n = int(input())
L, R = [], []
for i in range(n):
    a, b = 0, 0
    for c in input():
        if c == '(':
            b += 1
        if c == ')':
            if b > 0:
                b -= 1
            else:
                a += 1
    if -a + b > 0:
        L.append((a, b))
    else:
        R.append((a, b))
L.sort(key=lambda x: x[0])
R.sort(key=lambda x: x[1], reverse=True)
x = 0
for a, b in L + R:
    x -= a
    if x < 0:
        print('No')
        exit()
    x += b
if x == 0:
    print('Yes')
else:
    print('No')
