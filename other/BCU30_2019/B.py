n = int(input())
*A, = map(int, input().split())
s = 0
a = 0
for i in range(n):
    if (a == 0 or A[i] < a) and A[i] != 0:
        s += 1
    a = A[i]
print(s)
