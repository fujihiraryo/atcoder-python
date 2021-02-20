x = [int(c) for c in input()][::-1]
m = int(input())
k = len(x)
if k == 1:
    if x[0] <= m:
        print(1)
    else:
        print(0)
    exit()
n0 = max(x) + 1
if sum(x[i] * pow(n0, i) for i in range(k)) > m:
    print(0)
    exit()
n1 = n0 + m
while n1 - n0 > 1:
    n2 = (n0 + n1) // 2
    if sum(x[i] * pow(n2, i) for i in range(k)) <= m:
        n0 = n2
    else:
        n1 = n2
print(n0 - max(x))
