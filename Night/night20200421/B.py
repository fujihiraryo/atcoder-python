n = int(input())
*A, = map(int, input().split())
c = 0
for a in A:
    while a % 2 == 0:
        a = a//2
        c += 1
print(c)
