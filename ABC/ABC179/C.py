n = int(input())
D = [0] * n
for i in range(1, n):
    for j in range(i, n, i):
        D[j] += 1
print(sum(D))
