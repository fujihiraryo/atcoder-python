n = int(input())
a = [1] * (n + 1)
for i in range(1, n):
    for j in range(2 * i, n + 1, i):
        a[j] = a[i] + 1
print(*a[1:])
