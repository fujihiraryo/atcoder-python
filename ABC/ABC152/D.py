N = int(input())
d = len(str(N))
if d == 1:
    print(N)
    exit()
x = int(str(N)[0])
y = int(str(N)[-1])
if d == 2:
    M = 0
else:
    M = int(str(N)[1:-1])
count = 0
for A in range(1, N + 1):
    count0 = 0
    a = int(str(A)[0])
    b = int(str(A)[-1])
    if b == 0:
        continue
    if a == b:
        count0 += 1
    count0 += (10 ** (d - 2) - 1) // 9
    if b < x:
        count0 += 10 ** (d - 2)
    if b == x:
        count0 += M
        if a <= y:
            count0 += 1
    count += count0
print(count)
