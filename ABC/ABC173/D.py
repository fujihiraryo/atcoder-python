n = int(input())
*A, = map(int, input().split())
A.sort(reverse=True)
comfort = A[0]
j = 1
for i in range(n - 2):
    comfort += A[j]
    if i % 2 == 1:
        j += 1
print(comfort)
