def div(x):
    D = set()
    for i in range(1, int(x**0.5)+2):
        if x % i == 0:
            D.add(i)
            D.add(x//i)
    return D


n = int(input())
D0 = div(n)
D1 = div(n-1)
D0.remove(1)
D1.remove(1)
cnt = 0
for d in D0:
    tmp = n
    while tmp % d == 0:
        tmp = tmp // d
    if tmp % d == 1:
        cnt += 1
cnt += len(D1)
print(cnt)
